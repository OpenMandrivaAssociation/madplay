%define name 	madplay
%define version 0.15.2b
%define release 7

Summary:	Command line MPEG audio player based on libmad 
Name:		%{name}
Version:		%{version}
Release:		%{release}
Source0:		http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
License:		GPL
Group:		Sound
URL:		http://www.underbit.com/products/mad/
BuildRequires:  pkgconfig(mad) >= 0.15.0b
BuildRequires:  pkgconfig(id3tag) >= 0.15.0b
BuildRequires:  pkgconfig(esound)
Provides:	mad
Obsoletes:	mad

%description
madplay is a command-line MPEG audio decoder and player based on the
MAD library (libmad). For details about MAD, see the libmad package
distributed separately.

madplay will also read and display ID3 tag information, and further
supports the relative volume adjustment information (RVA2) in such
tags, as written by tools like `normalize'.


%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
# this is an invalid locale dir
rm -rf %buildroot/%{_datadir}/locale/en
%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README CREDITS TODO TODO
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Tue Aug 02 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.2b-7mdv2012.0
+ Revision: 692727
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.15.2b-6mdv2011.0
+ Revision: 251658
- rebuild

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 0.15.2b-4mdv2008.1
+ Revision: 140934
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.2b-4mdv2008.0
+ Revision: 55238
- Import madplay



* Thu Jul 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.2b-1mdv2007.0
- Rebuild

* Sun May 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.15.2b-3mdk
- Rebuild
- use mkrel

* Fri May 20 2005 Götz Waschk <waschk@mandriva.org> 0.15.2b-2mdk
- Rebuild

* Mon May 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.15.2b-1mdk
- spec fix
- fix source url
- New release 0.15.2b

* Sat Jul 19 2003 Götz Waschk <waschk@linux-mandrake.com> 0.15.0b-3mdk
- disable alsa (didn't work)

* Thu Jun 26 2003 Götz Waschk <waschk@linux-mandrake.com> 0.15.0b-2mdk
- fix url
- fix doc section

* Thu Jun 26 2003 Götz Waschk <waschk@linux-mandrake.com> 0.15.0b-1mdk
- obsolete the old mad
- autoconf 2.5 macro
- split out of the main mad package
- new version

* Wed May 21 2003 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-6mdk
- rebuild for provides

* Sun May  4 2003 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-5mdk
- devel package requires zlib-devel
- devel package requires pkgconfig
- mklibname macro

* Mon Oct 21 2002 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-4mdk
- arrgh, also add mad.pc

* Mon Oct 21 2002 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-3mdk
- add id3tag.pc from debian package (required by xmms-mad)

* Thu Jul 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.14.2b-2mdk
- add .la files

* Sat Jan 26 2002 Yves Duret <yduret@mandrakesoft.com> 0.14.2b-1mdk
- spec mandrakificazion: macros, standard libificazion, macros

* Sat Nov 10 2001 Götz Waschk <waschk@linux-mandrake.com> 0.14.2b-0.1mdk
- 0.14.2b

* Wed Nov  7 2001 Götz Waschk <waschk@linux-mandrake.com> 0.14.1b-0.1mdk
- 0.14.1b
- build shared library

* Fri Oct 19 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.14.0b-0.1mdk
- 0.14.0b

* Mon Sep 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.13.0-0.b1mdk
- added by Götz Waschk <waschk@linux-mandrake.com> :
        - initial package
