Name:		pysycache
Version:	3.1b
Release:	%mkrel 4
Group:		Education
Source0:	http://download.tuxfamily.org/py4childs/pysycache/v3.1/%{name}-src-%{version}.zip
Source1:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-ar-%{version}.zip
Source2:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-cs-%{version}.zip
Source3:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-da-%{version}.zip
Source4:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-de-%{version}.zip
Source5:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-en-%{version}.zip
Source6:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-es-%{version}.zip
Source7:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-fi-%{version}.zip
Source8:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-fr-%{version}.zip
Source9:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-it-%{version}.zip
Source10:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-lt-%{version}.zip
Source11:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-nl-%{version}.zip
Source12:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-pl-%{version}.zip
Source13:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-pt-%{version}.zip
Source14:	http://download.tuxfamily.org/py4childs/themes/themes-move/pack-lang-gpl-ru-%{version}.zip
URL:		http://www.pysycache.org/
Summary:	Educational point-and-click software for young children
License:	GPLv2+
BuildArch:	noarch
Requires:	pygame %{name}-language = %{version}
Buildrequires:	imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
PySyCache is an educational software for the young children (4-7 years old) 
with target to learn them to move the mouse to click with mouse buttons
PySyCache doesn't want some powerful computer, and it can be used 
at home with yours children in the schools

%package	lang-ar
Summary:	Arabic language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-ar
Arabic language pack for %{name}.

%package	lang-cs
Summary:	Czech language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-cs
Czech language pack for %{name}.

%package	lang-da
Summary:	Danish language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-da
Danish language pack for %{name}.

%package	lang-de
Summary:	German language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-de
German language pack for %{name}.

%package	lang-en
Summary:	English language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-en
English language pack for %{name}.

%package	lang-es
Summary:	Spanish language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-es
Spanish language pack for %{name}.

%package	lang-fi
Summary:	Finnish language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-fi
Finnish language pack for %{name}.

%package	lang-fr
Summary:	French language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-fr
French language pack for %{name}.

%package	lang-it
Summary:	Italian language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-it
Italian language pack for %{name}.

%package	lang-lt
Summary:	Lithuanian language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-lt
Lithuanian language pack for %{name}.

%package	lang-nl
Summary:	Dutch language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-nl
Dutch language pack for %{name}.

%package	lang-pl
Summary:	Polish language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description	lang-pl
Polish language pack for %{name}.

%package	lang-pt
Summary:	Portuguese language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description    lang-pt
Portuguese language pack for %{name}.

%package	lang-ru
Summary:	Russian language pack for %{name}
Provides:	%{name}-language = %{version}-%{release}
Requires:	%{name} = %{version}
Group:		Education

%description    lang-ru
Russian language pack for %{name}.

%prep
%setup -q -T -c %{name}-%{version} -a0
pushd pysycache-src/pysycache
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14}; do
	unzip -qq $i
done
popd

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_gamesdatadir}
cp -r pysycache-src/pysycache %{buildroot}%{_gamesdatadir}

install -d %{buildroot}%{_gamesbindir}
cat << EOF > %{buildroot}%{_gamesbindir}/%{name}
#!/bin/bash
cd
python %{_gamesdatadir}/pysycache/pysycache.py \$@
EOF
chmod +x %{buildroot}%{_gamesbindir}/%{name}

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Categories=X-MandrivaLinux-MoreApplications-Education;Education;
Name=PySyCache
Comment=%{Summary}
EOF

install -d %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -size 16x16 pysycache-src/pysycache/pysycache.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
convert -size 32x32 pysycache-src/pysycache/pysycache.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -size 48x48 pysycache-src/pysycache/pysycache.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/themes-move
%exclude %{_gamesdatadir}/%{name}/themes-move/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

%files lang-ar
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-ar
%{_gamesdatadir}/%{name}/themes-move/number-ar

%files lang-cs
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-cs
%{_gamesdatadir}/%{name}/themes-move/number-cs

%files lang-da
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-da
%{_gamesdatadir}/%{name}/themes-move/number-da

%files lang-de
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-de
%{_gamesdatadir}/%{name}/themes-move/number-de

%files lang-en
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-en
%{_gamesdatadir}/%{name}/themes-move/number-en

%files lang-es
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-es
%{_gamesdatadir}/%{name}/themes-move/number-es

%files lang-fi
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-fi
%{_gamesdatadir}/%{name}/themes-move/number-fi

%files lang-fr
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-fr
%{_gamesdatadir}/%{name}/themes-move/number-fr

%files lang-it
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-it
%{_gamesdatadir}/%{name}/themes-move/number-it

%files lang-lt
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-lt
%{_gamesdatadir}/%{name}/themes-move/number-lt

%files lang-nl
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-nl
%{_gamesdatadir}/%{name}/themes-move/number-nl

%files lang-pl
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-pl
%{_gamesdatadir}/%{name}/themes-move/number-pl

%files lang-pt
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-pt
%{_gamesdatadir}/%{name}/themes-move/number-pt

%files lang-ru
%defattr(644,root,root,755)
%{_gamesdatadir}/%{name}/themes-move/alphabet-ru
%{_gamesdatadir}/%{name}/themes-move/number-ru

