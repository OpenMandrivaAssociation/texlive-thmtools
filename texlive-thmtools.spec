# revision 26251
# category Package
# catalog-ctan /macros/latex/exptl/thmtools
# catalog-date 2012-04-27 11:57:13 +0200
# catalog-license lppl
# catalog-version 62
Name:		texlive-thmtools
Version:	62
Release:	11
Summary:	Extensions to theorem environments
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/exptl/thmtools
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.source.tar.xz
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
%{_texmfdistdir}/tex/latex/thmtools/aliasctr.sty
%{_texmfdistdir}/tex/latex/thmtools/parseargs.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-amsthm.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-autoref.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-beamer.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-kv.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-listof.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-llncs.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-ntheorem.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-patch.sty
%{_texmfdistdir}/tex/latex/thmtools/thm-restate.sty
%{_texmfdistdir}/tex/latex/thmtools/thmdef-mdframed.sty
%{_texmfdistdir}/tex/latex/thmtools/thmdef-shaded.sty
%{_texmfdistdir}/tex/latex/thmtools/thmdef-thmbox.sty
%{_texmfdistdir}/tex/latex/thmtools/thmtools.sty
%{_texmfdistdir}/tex/latex/thmtools/unique.sty
%doc %{_texmfdistdir}/doc/latex/thmtools/COPYING
%doc %{_texmfdistdir}/doc/latex/thmtools/README
%doc %{_texmfdistdir}/doc/latex/thmtools/TODO
%doc %{_texmfdistdir}/doc/latex/thmtools/VERSION.tex
%doc %{_texmfdistdir}/doc/latex/thmtools/thmtools-manual.tex
%doc %{_texmfdistdir}/doc/latex/thmtools/thmtools.pdf
#- source
%doc %{_texmfdistdir}/source/latex/thmtools/aliasctr.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/parseargs.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-amsthm.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-autoref.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-beamer.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-kv.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-listof.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-llncs.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-ntheorem.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-patch.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thm-restate.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thmdef-mdframed.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thmdef-shaded.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thmdef-thmbox.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thmtools.dtx
%doc %{_texmfdistdir}/source/latex/thmtools/thmtools.ins
%doc %{_texmfdistdir}/source/latex/thmtools/unique.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 62-3
+ Revision: 805110
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 62-2
+ Revision: 756834
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 62-1
+ Revision: 739940
- texlive-thmtools

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 59-1
+ Revision: 719730
- texlive-thmtools
- texlive-thmtools
- texlive-thmtools

