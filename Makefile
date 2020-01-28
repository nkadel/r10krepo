#
# Makefile - build wrapper for r10k on CentPOS 7
#
#	git clone RHEL 7 SRPM building tools from
#	https://github.com/nkadel/[package] into designated
#	R10KPKGS below
#
#	Set up local 

# Rely on local nginx service poingint to file://$(PWD)/r10krepo
REPOBASE = file://$(PWD)
#REPOBASE = http://localhost

# Compilable with EPEL
EPELPKGS+=rubygem-ansi-srpm
EPELPKGS+=rubygem-builder-srpm
#EPELPKGS+=rubygem-colored-srpm
EPELPKGS+=rubygem-colored2-srpm
EPELPKGS+=rubygem-cri-srpm
EPELPKGS+=rubygem-fattr-srpm
EPELPKGS+=rubygem-gettext-setup-srpm
EPELPKGS+=rubygem-json_pure-srpm
EPELPKGS+=rubygem-maruku-srpm
EPELPKGS+=rubygem-minitar-srpm
EPELPKGS+=rubygem-minitest-srpm
EPELPKGS+=rubygem-minitest4-srpm
EPELPKGS+=rubygem-puppet_forge-srpm
EPELPKGS+=rubygem-r10k-srpm
EPELPKGS+=rubygem-ruby-progressbar-srpm
EPELPKGS+=rubygem-session-srpm
EPELPKGS+=rubygem-timecop-srpm

# Requires other local packages

# Requires rubygem-ansi-srpm and rubygem-maruku-srpm
R10PKGSPKGS+=rubygem-minitest-reporters-srpm

# Requires rubygem-minitest > 5.0.0
R10PKGS+=rubygem-connection_pool-srpm

# Requires: rubygem-minitest-reporters
R10PKGS+=rubygem-zeitwerk-srpm

# Requires rubygem-timecop-srpm
R10KPKGS+=rubygem-concurrent-ruby-srpm

# Requires rubygem-concurrent-ruby
R10KPKGS+=rubygem-rb-inotify-srpm

# Requires rubygem-rb-notify
R10KPKGS+=rubygem-listen-srpm

# Requires rubygem-concurrent-ruby
# Requires rubygem-connection_pool
# Requires rubygem-listen
# Requires rubygem-minitest > 5.0.0
R10KPKGS+=rubygem-activesupport-srpm

# Requires rubygem-activesupport
R10KPKGS+=rubygem-activerecord-srpm

# Requires rubygem-activerecord
R10KPKGS+=rubygem-fast_gettext-srpm

# Requires rubygem-json_pure
R10KPKGS+=rubygem-multi_json-srpm

# Requires rubygem-builder
R10KPKGS+=rubygem-log4r-srpm

# Requires rubygem-minitest4
R10KPKGS+=rubygem-text-srpm

# Requires rubygem-session
R10KPKGS+=rubygem-rr-srpm

# Requires rubygem-rr
R10KPKGS+=rubygem-test-unit-rr-srpm

# Requires rubygem-rr
R10KPKGS+=rubygem-test-unit-notify-srpm

# Requires rubygem-test-unit-rr
R10KPKGS+=rubygem-locale-srpm

# Requires rubygem-text
R10KPKGS+=rubygem-gettext-srpm

REPOS+=r10krepo/el/7
REPOS+=r10krepo/el/8
REPOS+=r10krepo/fedora/31

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

# No local dependencies at build time
CFGS+=r10krepo-7-x86_64.cfg
CFGS+=r10krepo-8-x86_64.cfg
CFGS+=r10krepo-f31-x86_64.cfg

# Link from /etc/mock
MOCKCFGS+=epel-7-x86_64.cfg
MOCKCFGS+=epel-8-x86_64.cfg
MOCKCFGS+=fedora-31-x86_64.cfg

all:: $(CFGS) $(MOCKCFGS)
all:: $(REPODIRS)
all:: $(EPELPKGS)
all:: $(R10KPKGS)

.PHONY: all install clean getsrc
all install clean getsrc::
	@for name in $(EPELPKGS) $(R10KPKGS); do \
		pushd $$name; \
		$(MAKE) $(MFLAGS) $@; \
		popd; \
	done  

epel:: $(EPELPKGS)

# Build for locacl OS
.PHONY: build
build::
	@for name in $(R10KPKGS); do \
		pushd $$name; \
		$(MAKE) $(MFLAGS) $@; \
		popd; \
	done

# Dependencies

# Actually build in directories
.PHONY: $(EPELPKGS)
$(EPELPKGS)::
	(cd $@; $(MAKE) $(MLAGS) install)

.PHONY: $(R10KPKGS)
$(R10KPKGS)::
	(cd $@; $(MAKE) $(MLAGS) install)

repos: $(REPOS) $(REPODIRS)
$(REPOS):
	install -d -m 755 $@

.PHONY: $(REPODIRS)
$(REPODIRS): $(REPOS)
	@install -d -m 755 `dirname $@`
	/usr/bin/createrepo -q `dirname $@`


.PHONY: cfg cfgs
cfg cfgs:: $(CFGS) $(MOCKCFGS)

r10krepo-7-x86_64.cfg: /etc/mock/epel-7-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-7-x86_64/r10krepo-7-x86_64/g' $@
	@echo >> $@
	@echo "Disabling 'best=' for $@"
	@sed -i '/^best=/d' $@
	@echo "best=0" >> $@
	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
	@echo '[r10krepo]' >> $@
	@echo 'name=r10krepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/r10krepo/el/7/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=1' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@

r10krepo-8-x86_64.cfg: /etc/mock/epel-8-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/epel-8-x86_64/r10krepo-8-x86_64/g' $@
	@echo >> $@
	@echo "Disabling 'best=' for $@"
	@sed -i '/^best=/d' $@
	@echo "best=0" >> $@
	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
	@echo '[r10krepo]' >> $@
	@echo 'name=r10krepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/r10krepo/el/8/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=1' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@

r10krepo-f31-x86_64.cfg: /etc/mock/fedora-31-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i 's/fedora-31-x86_64/r10krepo-f31-x86_64/g' $@
	@echo >> $@
	@echo "Disabling 'best=' for $@"
	@sed -i '/^best=/d' $@
	@echo "best=0" >> $@
	@echo "config_opts['yum.conf'] += \"\"\"" >> $@
	@echo '[r10krepo]' >> $@
	@echo 'name=r10krepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/r10krepo/fedora/31/x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=1' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@

$(MOCKCFGS)::
	ln -sf --no-dereference /etc/mock/$@ $@

r10krepo.repo::
	if [ -s /etc/fedora-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/fedora/|g" > $@; \
	elif [ -s /etc/redhat-release ]; then \
		cat $@.in | \
			sed "s|@REPOBASEDIR@/|$(PWD)/|g" | \
			sed "s|/@RELEASEDIR@/|/el/|g" > $@; \
	else \
		echo Error: unknown release, check /etc/*-release; \
		exit 1; \
	fi

.PHONY: repo
repo:: r10krepo.repo /etc/yum.repos.d/r10krepo.repo
	cmp -s $? || echo 

clean::
	find . -name \*~ -exec rm -f {} \;
	rm -f *.cfg
	rm -f *.out
	rm -f nginx/default.d/*.conf
	@for name in $(R10KPKGS); do \
	    $(MAKE) -C $$name clean; \
	done

distclean:
	rm -rf $(REPOS)

maintainer-clean:
	rm -rf $(R10KPKGS)

FORCE::
