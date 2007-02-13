Summary:	Garble reciver data from GPS Garmin
Summary(pl.UTF-8):	Garble czytnik danych z GPS Gramin
Name:		garble
Version:	1.0.1
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.pdos.lcs.mit.edu/~decouto/garble/%{name}-%{version}.tar.gz
# Source0-md5:	a0479b213c64980a2d929e02b86dc275
URL:		http://www.pdos.lcs.mit.edu/~decouto/garble/
Conflicts:	gpsdrive
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Garble is a console program for downloading data (waypoints, proximity
waypoints, tracks, and routes) from Garmin GPS receivers. Garble is based on a
portable library that implements most of the Garmin communications protocol,
and supports most Garmin GPS receivers. Garble can also read the current time
and postion from the GPS, get the product data, and turn off the GPS. Garble
has been tested on a GPS 12XL (firmware 3.53) and a GPS III.

%description -l pl.UTF-8
Garble jest konsolowym programem służącym do zczytywania danych (punkty,
bliskość punktów, trasy, szlaki) z odbiorników GPS Garmin. Garble bazuje na
przenośnej bibliotece, która implementuje większość z protokołu
komunikacyjnego Garmin, wspieranego przez odbiorniki GPS Gramin. Garble 
potrafi także odczytać bieżący czas oraz aktualną pozycję, a także dane 
produktu, potrafi także wyłączyć sam odbiornik GPS. Garble zostało 
przetestowane z GPS 12XL (firmware 3.53) i GPS III.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install garble $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
