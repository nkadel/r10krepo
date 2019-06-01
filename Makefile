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
EPELPKGS+=rubygem-cri-srpm
EPELPKGS+=rubygem-colored-srpm
EPELPKGS+=rubygem-gettext-setup-srpm
EPELPKGS+=rubygem-r10k-srpm

# Actually compilable with epel-6-x86_64
#EPELPKGS+=python-r10k-srpm

REPOS+=r10krepo/el/7
REPOS+=r10krepo/el/8
REPOS+=r10krepo/fedora/30

REPODIRS := $(patsubst %,%/x86_64/repodata,$(REPOS)) $(patsubst %,%/SRPMS/repodata,$(REPOS))

# No local dependencies at build time
CFGS+=r10krepo-7-x86_64.cfg
CFGS+=r10krepo-8-x86_64.cfg
CFGS+=r10krepo-f30-x86_64.cfg

# Link from /etc/mock
MOCKCFGS+=epel-7-x86_64.cfg
MOCKCFGS+=epel-8-x86_64.cfg
MOCKCFGS+=fedora-30-x86_64.cfg

all:: $(CFGS) $(MOCKCFGS)
all:: $(REPODIRS)
all:: $(EPELPKGS)
all:: $(R10KPKGS)

all install clean:: FORCE
	@for name in $(EPELPKGS) $(R10KPKGS); do \
	     (cd $$name; $(MAKE) $(MFLAGS) $@); \
	done  

epel:: $(EPELPKGS)

# Build for locacl OS
build:: FORCE
	@for name in $(R10KPKGS); do \
	     (cd $$name; $(MAKE) $(MFLAGS) $@); \
	done

# Dependencies

# Actually build in directories
$(EPELPKGS):: FORCE
	(cd $@; $(MAKE) $(MLAGS) install)

$(R10KPKGS):: FORCE
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
	@echo '"""' >> $@
	@echo >> $@
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
	@uniq -u $@ > $@~
	@mv $@~ $@

r10krepo-8-x86_64.cfg: /etc/mock/epel-8-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i "s/'epel-8-x86_64'/'r10krepo-8-x86_64'/g" $@
	@echo '"""' >> $@
	@echo >> $@
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
	@uniq -u $@ > $@~
	@mv $@~ $@

r10krepo-f30-x86_64.cfg: /etc/mock/fedora-30-x86_64.cfg
	@echo Generating $@ from $?
	@cat $? > $@
	@sed -i "s/'fedora-30-x86_64'/'r10krepo-f30-x86_64'/g" $@
	@echo '"""' >> $@
	@echo >> $@
	@echo '[r10krepo]' >> $@
	@echo 'name=r10krepo' >> $@
	@echo 'enabled=1' >> $@
	@echo 'baseurl=$(REPOBASE)/r10krepo/fedora/30x86_64/' >> $@
	@echo 'failovermethod=priority' >> $@
	@echo 'skip_if_unavailable=False' >> $@
	@echo 'metadata_expire=1' >> $@
	@echo 'gpgcheck=0' >> $@
	@echo '#cost=2000' >> $@
	@echo '"""' >> $@
	@uniq -u $@ > $@~
	@mv $@~ $@

$(MOCKCFGS)::
	ln -sf --no-dereference /etc/mock/$@ $@

repo: r10krepo.repo
r10krepo.repo:: Makefile r10krepo.repo.in
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

r10krepo.repo:: FORCE
	cmp -s /etc/yum.repos.d/$@ $@       


nginx:: nginx/default.d/r10krepo.conf

nginx/default.d/r10krepo.conf:: FORCE nginx/default.d/r10krepo.conf.in
	cat $@.in | \
		sed "s|@REPOBASEDIR@;|$(PWD)/;|g" | tee $@;

nginx/default.d/r10krepo.conf:: FORCE
	cmp -s $@ /etc/$@ || \
	    diff -u $@ /etc/$@

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
