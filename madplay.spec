Summary:	Command line MPEG audio player based on libmad 
Name:		madplay
Version:	0.15.2b
Release:	10
Source0:	http://prdownloads.sourceforge.net/mad/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Sound
URL:		https://www.underbit.com/products/mad/
BuildRequires:  pkgconfig(mad) >= 0.15.0b
BuildRequires:  pkgconfig(id3tag) >= 0.15.0b
BuildRequires:  pkgconfig(esound)
%rename		mad

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
rm -rf %{buildroot}/%{_datadir}/locale/en
%find_lang %{name}

%files -f %{name}.lang
%doc COPYING README CREDITS TODO 
%{_bindir}/*
%{_mandir}/man1/*


