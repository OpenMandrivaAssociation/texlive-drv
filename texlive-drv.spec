# revision 21499
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/drv
# catalog-date 2011-02-22 19:59:57 +0100
# catalog-license lppl
# catalog-version 0.97
Name:		texlive-drv
Version:	0.97
Release:	1
Summary:	Derivation trees with MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/drv
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drv.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/drv.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A set of MetaPost macros for typesetting derivation trees (such
as used in sequent calculus, type inference, programming
language semantics...). No MetaPost knowledge is needed to use
these macros.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/drv/drv.mp
%doc %{_texmfdistdir}/doc/metapost/drv/README
%doc %{_texmfdistdir}/doc/metapost/drv/doc/drv-guide.mp
%doc %{_texmfdistdir}/doc/metapost/drv/doc/drv-guide.tex
%doc %{_texmfdistdir}/doc/metapost/drv/doc/drv.mp
%doc %{_texmfdistdir}/doc/metapost/drv/doc/makefile
%doc %{_texmfdistdir}/doc/metapost/drv/doc/readme.sh
%doc %{_texmfdistdir}/doc/metapost/drv/drv-guide.pdf
%doc %{_texmfdistdir}/doc/metapost/drv/sample/coq-sample.mp
%doc %{_texmfdistdir}/doc/metapost/drv/sample/coq-sample.tex
%doc %{_texmfdistdir}/doc/metapost/drv/sample/drv.mp
%doc %{_texmfdistdir}/doc/metapost/drv/sample/makefile
%doc %{_texmfdistdir}/doc/metapost/drv/sample/readme.sh
%doc %{_texmfdistdir}/doc/metapost/drv/template/drv.mp
%doc %{_texmfdistdir}/doc/metapost/drv/template/makefile
%doc %{_texmfdistdir}/doc/metapost/drv/template/readme.sh
%doc %{_texmfdistdir}/doc/metapost/drv/template/template.mp
%doc %{_texmfdistdir}/doc/metapost/drv/template/template.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
