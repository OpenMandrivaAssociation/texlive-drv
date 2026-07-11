%global tl_name drv
%global tl_revision 29349

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.97
Release:	%{tl_revision}.1
Summary:	Derivation trees with MetaPost
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/drv
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/drv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A set of MetaPost macros for typesetting derivation trees (such as used
in sequent calculus, type inference, programming language semantics...).
No MetaPost knowledge is needed to use these macros.

