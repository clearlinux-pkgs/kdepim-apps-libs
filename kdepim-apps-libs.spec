#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kdepim-apps-libs
Version  : 19.08.0
Release  : 15
URL      : https://download.kde.org/stable/applications/19.08.0/src/kdepim-apps-libs-19.08.0.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.0/src/kdepim-apps-libs-19.08.0.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.0/src/kdepim-apps-libs-19.08.0.tar.xz.sig
Summary  : KDE PIM mail related libraries
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kdepim-apps-libs-data = %{version}-%{release}
Requires: kdepim-apps-libs-lib = %{version}-%{release}
Requires: kdepim-apps-libs-license = %{version}-%{release}
Requires: kdepim-apps-libs-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : kcontacts-dev
BuildRequires : kimap-dev
BuildRequires : kimap-staticdev
BuildRequires : kmime-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : pimcommon-dev
BuildRequires : prison-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the kdepim-apps-libs package.
Group: Data

%description data
data components for the kdepim-apps-libs package.


%package dev
Summary: dev components for the kdepim-apps-libs package.
Group: Development
Requires: kdepim-apps-libs-lib = %{version}-%{release}
Requires: kdepim-apps-libs-data = %{version}-%{release}
Provides: kdepim-apps-libs-devel = %{version}-%{release}
Requires: kdepim-apps-libs = %{version}-%{release}
Requires: kdepim-apps-libs = %{version}-%{release}

%description dev
dev components for the kdepim-apps-libs package.


%package lib
Summary: lib components for the kdepim-apps-libs package.
Group: Libraries
Requires: kdepim-apps-libs-data = %{version}-%{release}
Requires: kdepim-apps-libs-license = %{version}-%{release}

%description lib
lib components for the kdepim-apps-libs package.


%package license
Summary: license components for the kdepim-apps-libs package.
Group: Default

%description license
license components for the kdepim-apps-libs package.


%package locales
Summary: locales components for the kdepim-apps-libs package.
Group: Default

%description locales
locales components for the kdepim-apps-libs package.


%prep
%setup -q -n kdepim-apps-libs-19.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1565930511
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1565930511
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdepim-apps-libs
cp COPYING %{buildroot}/usr/share/package-licenses/kdepim-apps-libs/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kdepim-apps-libs/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libkaddressbookgrantlee
%find_lang libsendlater
%find_lang libkaddressbookimportexport

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kdepim-apps-lib.categories
/usr/share/qlogging-categories5/kdepim-apps-lib.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/FollowupReminder/FollowUpReminderInfo
/usr/include/KF5/FollowupReminder/FollowUpReminderUtil
/usr/include/KF5/KAddressBookImportExport/KAddressBookContactSelectionDialog
/usr/include/KF5/KAddressBookImportExport/KAddressBookContactSelectionWidget
/usr/include/KF5/KAddressBookImportExport/KAddressBookExportSelectionWidget
/usr/include/KF5/KAddressBookImportExport/KAddressBookImportExportContactList
/usr/include/KF5/KAddressBookImportExport/KAddressBookImportExportPlugin
/usr/include/KF5/KAddressBookImportExport/KAddressBookImportExportPluginInterface
/usr/include/KF5/KAddressBookImportExport/KAddressBookImportExportPluginManager
/usr/include/KF5/KaddressbookGrantlee/GrantleeContactFormatter
/usr/include/KF5/KaddressbookGrantlee/GrantleeContactGroupFormatter
/usr/include/KF5/KaddressbookGrantlee/GrantleeContactViewer
/usr/include/KF5/KaddressbookGrantlee/GrantleePrint
/usr/include/KF5/KdepimDBusInterfaces/ReminderClient
/usr/include/KF5/KdepimDBusInterfaces/UriHandler
/usr/include/KF5/SendLater/SendLaterDialog
/usr/include/KF5/SendLater/SendLaterInfo
/usr/include/KF5/SendLater/SendLaterUtil
/usr/include/KF5/followupreminder/followupreminder_export.h
/usr/include/KF5/followupreminder/followupreminderagentsettings.h
/usr/include/KF5/followupreminder/followupreminderinfo.h
/usr/include/KF5/followupreminder/followupreminderutil.h
/usr/include/KF5/followupreminder_version.h
/usr/include/KF5/kaddressbookgrantlee/grantleecontactformatter.h
/usr/include/KF5/kaddressbookgrantlee/grantleecontactgroupformatter.h
/usr/include/KF5/kaddressbookgrantlee/grantleecontactviewer.h
/usr/include/KF5/kaddressbookgrantlee/grantleeprint.h
/usr/include/KF5/kaddressbookgrantlee/kaddressbook_grantlee_export.h
/usr/include/KF5/kaddressbookgrantlee_version.h
/usr/include/KF5/kaddressbookimportexport/kaddressbook_importexport_export.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookcontactselectiondialog.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookcontactselectionwidget.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookexportselectionwidget.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookimportexportcontactfields.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookimportexportcontactlist.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookimportexportplugin.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookimportexportplugininterface.h
/usr/include/KF5/kaddressbookimportexport/kaddressbookimportexportpluginmanager.h
/usr/include/KF5/kaddressbookimportexport_version.h
/usr/include/KF5/kdepimdbusinterfaces/kdepimdbusinterfaces_export.h
/usr/include/KF5/kdepimdbusinterfaces/reminderclient.h
/usr/include/KF5/kdepimdbusinterfaces/urihandler.h
/usr/include/KF5/kdepimdbusinterfaces_version.h
/usr/include/KF5/sendlater/sendlater_export.h
/usr/include/KF5/sendlater/sendlateragentsettings.h
/usr/include/KF5/sendlater/sendlaterdialog.h
/usr/include/KF5/sendlater/sendlaterinfo.h
/usr/include/KF5/sendlater/sendlaterutil.h
/usr/include/KF5/sendlater_version.h
/usr/lib64/cmake/KF5FollowupReminder/KF5FollowupReminderConfig.cmake
/usr/lib64/cmake/KF5FollowupReminder/KF5FollowupReminderConfigVersion.cmake
/usr/lib64/cmake/KF5FollowupReminder/KF5FollowupReminderTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5FollowupReminder/KF5FollowupReminderTargets.cmake
/usr/lib64/cmake/KF5KaddressbookGrantlee/KF5KaddressbookGrantleeConfig.cmake
/usr/lib64/cmake/KF5KaddressbookGrantlee/KF5KaddressbookGrantleeConfigVersion.cmake
/usr/lib64/cmake/KF5KaddressbookGrantlee/KF5KaddressbookGrantleeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KaddressbookGrantlee/KF5KaddressbookGrantleeTargets.cmake
/usr/lib64/cmake/KF5KaddressbookImportExport/KF5KaddressbookImportExportConfig.cmake
/usr/lib64/cmake/KF5KaddressbookImportExport/KF5KaddressbookImportExportConfigVersion.cmake
/usr/lib64/cmake/KF5KaddressbookImportExport/KF5KaddressbookImportExportTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KaddressbookImportExport/KF5KaddressbookImportExportTargets.cmake
/usr/lib64/cmake/KF5KdepimDBusInterfaces/KF5KdepimDBusInterfacesConfig.cmake
/usr/lib64/cmake/KF5KdepimDBusInterfaces/KF5KdepimDBusInterfacesConfigVersion.cmake
/usr/lib64/cmake/KF5KdepimDBusInterfaces/KF5KdepimDBusInterfacesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5KdepimDBusInterfaces/KF5KdepimDBusInterfacesTargets.cmake
/usr/lib64/cmake/KF5SendLater/KF5SendLaterConfig.cmake
/usr/lib64/cmake/KF5SendLater/KF5SendLaterConfigVersion.cmake
/usr/lib64/cmake/KF5SendLater/KF5SendLaterTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5SendLater/KF5SendLaterTargets.cmake
/usr/lib64/libKF5FollowupReminder.so
/usr/lib64/libKF5KaddressbookGrantlee.so
/usr/lib64/libKF5KaddressbookImportExport.so
/usr/lib64/libKF5KdepimDBusInterfaces.so
/usr/lib64/libKF5SendLater.so
/usr/lib64/qt5/mkspecs/modules/qt_FollowupReminder.pri
/usr/lib64/qt5/mkspecs/modules/qt_KaddressbookGrantlee.pri
/usr/lib64/qt5/mkspecs/modules/qt_KaddressbookImportExport.pri
/usr/lib64/qt5/mkspecs/modules/qt_KdepimDBusInterfaces.pri
/usr/lib64/qt5/mkspecs/modules/qt_SendLater.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5FollowupReminder.so.5
/usr/lib64/libKF5FollowupReminder.so.5.12.0
/usr/lib64/libKF5KaddressbookGrantlee.so.5
/usr/lib64/libKF5KaddressbookGrantlee.so.5.12.0
/usr/lib64/libKF5KaddressbookImportExport.so.5
/usr/lib64/libKF5KaddressbookImportExport.so.5.12.0
/usr/lib64/libKF5KdepimDBusInterfaces.so.5
/usr/lib64/libKF5KdepimDBusInterfaces.so.5.12.0
/usr/lib64/libKF5SendLater.so.5
/usr/lib64/libKF5SendLater.so.5.12.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdepim-apps-libs/COPYING
/usr/share/package-licenses/kdepim-apps-libs/COPYING.LIB

%files locales -f libkaddressbookgrantlee.lang -f libsendlater.lang -f libkaddressbookimportexport.lang
%defattr(-,root,root,-)

