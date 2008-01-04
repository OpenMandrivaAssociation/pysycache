%define	name	pysycache
%define	version	2.0
%define	release	%mkrel 3
%define	Summary	Educational point-and-click software for young children

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Education
Source0:	http://www.pysycache.org/telechargement/v%{version}/%{name}-%{version}.tar.bz2
Source21:	http://download.gna.org/py4childs/pysycache/v%{version}/%{name}-lang-de-%{version}.zip
Source22:	http://download.gna.org/py4childs/pysycache/v%{version}/%{name}-lang-it-%{version}.zip
Source23:	http://download.gna.org/py4childs/pysycache/v%{version}/%{name}-lang-es-%{version}.zip
Source24:	http://download.gna.org/py4childs/pysycache/v%{version}/%{name}-lang-fr-%{version}.zip
Source25:	http://download.gna.org/py4childs/pysycache/v%{version}/%{name}-lang-pt-%{version}.zip
Url:		http://www.pysycache.org/
Summary:	%{Summary}
License:	GPL
BuildArch:	noarch
Requires:	pygame %{name}-language = %{version}
Buildrequires:	ImageMagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PySyCache is an educational software for the young children (4-7 years old) 
with target to learn them to move the mouse to click with mouse buttons
PySyCache doesn't want some powerful computer, and it can be used 
at home with yours children in the schools

%package	lang-en
Summary:	English language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-en
English language pack for %{name}.

%package	lang-fr
Summary:        French language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-fr
French language pack for %{name}.

%package	lang-de
Summary:	German language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-de
German language pack for %{name}.

%package	lang-it
Summary:	Italian language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description    lang-it
Italian language pack for %{name}.

%package        lang-es
Summary:        Estonian language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description    lang-es
Estonian language pack for %{name}.

%package	lang-pt
Summary:	Portugese language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description    lang-pt
Portugese language pack for %{name}.


%prep
%setup -q -T -c %{name}-%{version} -a0
cd usr/local/share/pysycache
for i in %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{SOURCE25}; do
	unzip $i
done

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_gamesdatadir}
cp -r usr/local/share/pysycache %{buildroot}%{_gamesdatadir}

install -d %{buildroot}%{_gamesbindir}
cat << EOF > %{buildroot}%{_gamesbindir}/%{name}
#!/bin/bash
cd
python %{_gamesdatadir}/pysycache/pysycache.py \$@
EOF
chmod +x %{buildroot}%{_gamesbindir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=Amusement;
Name=PySyCache
Comment=%{Summary}
EOF

install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -size 16x16 usr/share/pixmaps/pysycache.png %{buildroot}%{_miconsdir}/%{name}.png
convert -size 32x32 usr/share/pixmaps/pysycache.png %{buildroot}%{_iconsdir}/%{name}.png
convert -size 48x48 usr/share/pixmaps/pysycache.png %{buildroot}%{_liconsdir}/%{name}.png

install -m644 usr/share/applnk/Games/pysycache.desktop -D %{buildroot}%{_datadir}/applnk/Games/pysycache.desktop
install -m644 usr/share/gnome/apps/Games/pysycache.desktop -D %{buildroot}%{_datadir}/gnome/apps/Games/pysycache.desktop
install -m644 usr/share/pixmaps/pysycache.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/themes-move
%exclude %{_gamesdatadir}/%{name}/themes-move/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applnk/Games/pysycache.desktop
%{_datadir}/gnome/apps/Games/pysycache.desktop
%{_datadir}/pixmaps/%{name}.png

%files lang-en
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-en
%{_gamesdatadir}/%{name}/themes-move/number-en

%files lang-fr
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-fr
%{_gamesdatadir}/%{name}/themes-move/number-fr

%files lang-de
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-de
%{_gamesdatadir}/%{name}/themes-move/number-de

%files lang-it
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-it
%{_gamesdatadir}/%{name}/themes-move/number-it

%files lang-es
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-es
%{_gamesdatadir}/%{name}/themes-move/number-es

%files lang-pt
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-pt
%{_gamesdatadir}/%{name}/themes-move/number-pt


