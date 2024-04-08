# Generated by rust2rpm 25
%bcond_without check

%global crate vhost-device-sound

Name:           rust-vhost-device-sound
Version:        0.1.0
Release:        %autorelease
Summary:        Virtio sound device using the vhost-user protocol

License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/vhost-device-sound
Source:         %{crates_source}

# Manually created patch to ignore pipewire server test
Patch0:          ignore-pw-server-test.patch
# Alsa unit test fails on x86_64
Patch1: build-fix-for-alsa-test.patch
#  Convert i64 values to i32
Patch2: build-fix-for-i386.patch
# Upstream doesn't provide man pages
Patch3: man-page.patch

# Package dependencies vmm-sys-util not built for s390x
ExcludeArch: s390x

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  dbus-daemon >= 1.14.10

%global _description %{expand:
A virtio sound device using the vhost-user protocol.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# FIXME: paste output of %%cargo_license_summary here
License:        (Apache-2.0 OR BSD-3-Clause) AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSD-3-Clause AND MIT AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE-APACHE
%license LICENSE-BSD-3-Clause
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/vhost-device-sound

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-BSD-3-Clause
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alsa-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alsa-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "alsa-backend" feature of the "%{crate}" crate.

%files       -n %{name}+alsa-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pw-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pw-devel %{_description}

This package contains library source intended for building other packages which
use the "pw" feature of the "%{crate}" crate.

%files       -n %{name}+pw-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pw-backend-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pw-backend-devel %{_description}

This package contains library source intended for building other packages which
use the "pw-backend" feature of the "%{crate}" crate.

%files       -n %{name}+pw-backend-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+xen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+xen-devel %{_description}

This package contains library source intended for building other packages which
use the "xen" feature of the "%{crate}" crate.

%files       -n %{name}+xen-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%setup -n %{crate}-%{version}
%patch 0 -p1
%patch 1 -p1
%ifarch i386
%patch 2 -p1
%endif
%patch 3 -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
# * test does not panic
%cargo_test -- -- --exact --skip result::tests::async_seq_panic
%endif

%changelog
%autochangelog
