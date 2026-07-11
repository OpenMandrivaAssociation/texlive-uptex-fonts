%global tl_name uptex-fonts
%global tl_revision 74119

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Fonts for use with upTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/uptex-fonts
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-fonts.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-fonts.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle contains fonts (TFM and VF) for use with upTeX. This is a
redistribution derived from the upTeX distribution by Takuji Tanaka.

