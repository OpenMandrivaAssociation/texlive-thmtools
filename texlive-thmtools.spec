Name:		texlive-thmtools
Version:	63477
Release:	1
Summary:	Extensions to theorem environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/thmtools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides several packages for commonly-needed
support for typesetting theorems. The packages should work with
kernel theorems (theorems 'out of the box' with LaTeX), and the
theorem and amsthm packages. Features of the bundle include: -
a key-value interface to \newtheorem; - a \listoftheorems
command; - hyperref and autoref compatibility; - a mechanism
for restating entire theorems in a single macro call.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/thmtools
%doc %{_texmfdistdir}/doc/latex/thmtools
#- source
%doc %{_texmfdistdir}/source/latex/thmtools

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
