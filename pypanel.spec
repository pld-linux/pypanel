Summary:	Lightweight panel/taskbar for X11
Summary(pl):	Lekki panel dla X11
Name:		pypanel
Version:	0.9
Release:	1
License:	GNU
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/pypanel/PyPanel-%{version}.tar.gz
# Source0-md5:	622c01f053f90167fcfd996f5cf8f772
Patch0:		%{name}-path.patch
URL:		http://pypanel.sourceforge.net/
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyPanel is a lightweight panel/taskbar for X11 window managers that
can be easily customized to match any desktop theme or taste.

Some of the customizable features include:
- Transparency w/ shading
- Panel dimensions and location
- Font type and colors
- Button events/actions
- Clock and workspace name display

%description -l pl
PyPanel jest lekkim panelem/paskiem zada� dla zarz�dc�w okien systemu
X11. PyPanel mo�e by� �atwo dostosowany do dowolnego gustu czy tematu
pulpitu.

PyPanel oferuje mi�dzy innymi:
- przezroczysto�� z cieniowaniem
- ustalanie po�o�enia i wymiar�w panelu
- wyb�r rodzaju i kolor�w czcionki
- zdarzenia przycisk�w
- wy�wietlanie zegara i nazwy pulpitu

%prep
%setup -q -n PyPanel-%{version}
%patch0 -p1

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{py_sitedir}/*.so
