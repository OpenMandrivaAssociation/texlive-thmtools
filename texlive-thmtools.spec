%global tl_name thmtools
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	76
Release:	%{tl_revision}.1
Summary:	Extensions to theorem environments
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thmtools
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thmtools.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides several packages for commonly-needed support for
typesetting theorems. The packages should work with kernel theorems
(theorems 'out of the box' with LaTeX), and the theorem and amsthm
packages. Features of the bundle include: a key-value interface to
\newtheorem; a \listoftheorems command; hyperref and autoref
compatibility; a mechanism for restating entire theorems in a single
macro call.

