%define name 	madplay
%define version 0.15.2b
%define release %mkrel 6

Summary:	Command line MPEG audio player based on libmad 
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Sound
URL:		http://www.underbit.com/products/mad/
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:  libmad-devel >= 0.15.0b
BuildRequires:  libid3tag-devel >= 0.15.0b
BuildRequires:  libesound-devel
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
rm -rf %buildroot
%makeinstall
# this is an invalid locale dir
rm -rf %buildroot/%{_datadir}/locale/en
%find_lang %{name}

%clean
rm -fr %buildroot


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README CREDITS TODO TODO
%{_bindir}/*
%{_mandir}/man1/*
