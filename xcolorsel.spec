%define name xcolorsel
%define version 1.1a
%define release %mkrel 5

Summary: Simple color displayer/selector for X11 rgb.txt files
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}-src.tar.gz
Patch0: xcolorsel_1.1a-16_debian.patch
Patch1: xcolorsel_rgbtxt-mdv.patch
License: GPLv2+
Group: Graphics
Url: ftp://ftp.x.org/contrib/utilities/xcolorsel-1.1a-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: imake
BuildRequires: gccmakedep
BuildRequires: Xaw3d-devel
BuildRequires: libxmu-devel
BuildRequires: libxt-devel
BuildRequires: libxpm-devel
BuildRequires: libxp-devel
BuildRequires: libxext-devel
BuildRequires: libxau-devel
BuildRequires: libxdmcp-devel

%description
xcolorsel is a X-Utility that allows you to display X11 "rgb.txt" or
other such files together with tiles showing how the color looks on
your screen. Also a programmer may (like with xfontsel) cut the color
names/definitions in various formats (Colorformats and formats for
resourcefiles or C-sources) und paste them directly in his source
codes.

%prep
%setup -q -n xcolorsel
%patch0 -p1
%patch1 -p1

%build
xmkmf -a
# XAWLIB=-lXaw3d taken from Debian, otherwise it links with libxaw and crashes at runtime
%make XAWLIB=-lXaw3d

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot/%_prefix/lib/X11/app-defaults

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc 00-ANNOUNCE 00-README 01-CHANGELOG 01-COPYING
%_sysconfdir/X11/app-defaults/Xcolorsel
%_sysconfdir/X11/app-defaults/Xcolorsel-color
%_bindir/xcolorsel
%_prefix/lib/X11/xcolorsel/Xcolorsel.help


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-5mdv2010.0
+ Revision: 435067
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-4mdv2009.0
+ Revision: 262281
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.1a-3mdv2009.0
+ Revision: 256677
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.1a-1mdv2008.1
+ Revision: 140953
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Gustavo De Nardin <gustavodn@mandriva.com> 1.1a-1mdv2008.0
+ Revision: 74600
- fixed BuildRequires on Xaw3d
- 1st Mandriva xcolorsel version imported into SVN

