%define		_plugin	saconf
%define		mversion	1.2.7
Summary:	SquirrelMail plugin that allows to configure the behavior of the SpamAssassin
Summary(pl.UTF-8):	Wtyczka dla SquirrelMaila pozwalająca kontrolować zachowanie SpamAssassina
Name:		squirrelmail-plugin-%{_plugin}
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.squirrelmail.org/plugins/%{_plugin}.%{version}-%{mversion}.tar.gz
# Source0-md5:	cd5dc5d89fa6827a5b662525b16afc89
URL:		http://www.squirrelmail.org/plugin_view.php?id=111
Requires:	php(ftp)
Requires:	squirrelmail >= 1.4.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_datadir}/squirrelmail/plugins/%{_plugin}
%define		_sysconfdir	/etc/webapps/squirrelmail

%description
SAConf is a SquirrelMail plugin that allows users to configure the
behavior of the SpamAssassin mail filter. Specifically SAConf can
modify a user's spam threshold value, whitelist contents, and
destination folder for spam. SAConf connects to the mail server via
FTP and modifies the user's .procmailrc and .spamassassin/user_prefs
files. FTP support in PHP is required to use SAConf.

%description -l pl.UTF-8
SAConf to wtyczka SquirrelMaila umożliwiająca kontrolowanie zachowania
SpamAssassina (w szczególności wartości progowej, zawartości białej
listy i folderu na spam) poprzez modyfikację plików .procmailrc i
.spamassassin/user_prefs w katalogu użytkownika. Wymagana jest obsługa
prokotołu FTP w PHP.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir} $RPM_BUILD_ROOT%{_sysconfdir}

install *.php $RPM_BUILD_ROOT%{_plugindir}
rm -rf saconf_options.php~
mv $RPM_BUILD_ROOT%{_plugindir}/saconf_conf.php $RPM_BUILD_ROOT%{_sysconfdir}/saconf_conf.php
ln -s %{_sysconfdir}/saconf_conf.php $RPM_BUILD_ROOT%{_plugindir}/saconf_conf.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/saconf_conf.php
%dir %{_plugindir}
%{_plugindir}/*.php
