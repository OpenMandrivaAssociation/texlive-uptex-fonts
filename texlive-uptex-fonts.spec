Name:		texlive-uptex-fonts
Version:	62592
Release:	2
Summary:	Fonts for use with upTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uptex-fonts
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-fonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex-fonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle contains fonts (TFM and VF) for use with upTeX. This
is a redistribution derived from the upTeX distribution by
Takuji Tanaka.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/vf/uptex-fonts
%{_texmfdistdir}/fonts/tfm/uptex-fonts
%doc %{_texmfdistdir}/fonts/source/uptex-fonts
%{_texmfdistdir}/fonts/cmap/uptex-fonts
%doc %{_texmfdistdir}/doc/fonts/uptex-fonts

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
