#!/bin/python3
from flask import Flask

from webscripts.ServerManager import *

app = Flask(__name__,
            template_folder='static/templates',  # static imgs/html/css
            static_folder='static')  # entire static


# the 'ServerManager' directory in server
sm_path = '/ServerManager/'


@app.route(sm_path+'Login')
def Login_page():
    """the /ServerManager/Login page which is responsible
     of authenticate the user of the app."""
    # TODO Login (user,pass) from POST
    return Login.load_page()


@app.route('/')  # TODO redirect instead of route
@app.route(sm_path)  # TODO redirect instead of route
@app.route(sm_path+'Dashboard')
def Dashboard_page():
    """the /ServerManager/Dashboard page is Default site 
    of the app."""
    return Dashboard.load_page()


@app.route(sm_path+'AllServers')
def AllServers_page():
    """the /ServerManager/AllServers page contains all servers information."""
    return AllServers.load_page()


@app.route(sm_path+'LocalServer')
def LocalServer_page():
    """the /ServerManager/LocalServer page contains local server information."""
    return LocalServer.load_page()


# the 'ServerManager/ActiveDirectoryDomainServicesConfigurationWizard' directory in server
addscw_path = sm_path+'ActiveDirectoryDomainServicesConfigurationWizard/'


@app.route(addscw_path)  # TODO redirect instead of route
@app.route(addscw_path+'DeploymentConfigurations')
def DeploymentConfigurations_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/DeploymentConfigurations page is the first page in the wizard."""
    return DeploymentConfigurations.load_page()


@app.route(addscw_path+'AdditionalOptions')
def AdditionalOptions_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/AdditionalOptions page is a page in the wizard."""
    return AdditionalOptions.load_page()@app.route(addscw_path+'AdditionalOptions')

@app.route(addscw_path+'DomainControllerOptions')
def DomainControllerOptions_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/DomainControllerOptions page is a page in the wizard."""
    return DomainControllerOptions.load_page()


@app.route(addscw_path+'DNSOptions')
def DNSOptions_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/DNSOptions page is a page in the wizard."""
    return DNSOptions.load_page()


@app.route(addscw_path+'Installation')
def Installation_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/Installation page is a page in the wizard."""
    return Installation.load_page()


@app.route(addscw_path+'Paths')
def Paths_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/Paths page is a page in the wizard."""
    return Paths.load_page()


@app.route(addscw_path+'PrerequisitesCheck')
def PrerequisitesCheck_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/PrerequisitesCheck page is a page in the wizard."""
    return PrerequisitesCheck.load_page()


@app.route(addscw_path+'ReviewOptions')
def ReviewOptions_page():
    """the /ServerManager/ActiveDirectoryDomainServicesConfigurationWizard/ReviewOptions page is a page in the wizard."""
    return ReviewOptions.load_page()


# the 'ServerManager/AddRolesandFeturesWizard' directory in server
arfw_path = sm_path+'AddRolesandFeturesWizard/'


@app.route(arfw_path)  # TODO redirect instead of route
@app.route(arfw_path+'Beforeyoubegin')
def Beforeyoubegin_page():
    """the /ServerManager/AddRolesandFeturesWizard/Beforeyoubegin page is a page in the wizard."""
    return Beforeyoubegin.load_page()


@app.route(arfw_path+'ADLDS')
def ADLDS_page():
    """the /ServerManager/AddRolesandFeturesWizard/ADLDS page is a page in the wizard."""
    return ADLDS.load_page()


@app.route(arfw_path+'Confirmation')
def Confirmation_page():
    """the /ServerManager/AddRolesandFeturesWizard/Confirmation page is a page in the wizard."""
    return Confirmation.load_page()


@app.route(arfw_path+'DNSServer')
def DNSServer_page():
    """the /ServerManager/AddRolesandFeturesWizard/DNSServer page is a page in the wizard."""
    return DNSServer.load_page()


@app.route(arfw_path+'Features')
def Features_page():
    """the /ServerManager/AddRolesandFeturesWizard/Features page is a page in the wizard."""
    return Features.load_page()


@app.route(arfw_path+'InstallationType')
def InstallationType_page():
    """the /ServerManager/AddRolesandFeturesWizard/InstallationType page is a page in the wizard."""
    return InstallationType.load_page()


@app.route(arfw_path+'Result')
def Result_page():
    """the /ServerManager/AddRolesandFeturesWizard/Result page is a page in the wizard."""
    return Result.load_page()


@app.route(arfw_path+'ServerRoles')
def ServerRoles_page():
    """the /ServerManager/AddRolesandFeturesWizard/ServerRoles page is a page in the wizard."""
    return ServerRoles.load_page()


@app.route(arfw_path+'ServerSelection')
def ServerSelection_page():
    """the /ServerManager/AddRolesandFeturesWizard/ServerSelection page is a page in the wizard."""
    return ServerSelection.load_page()


# the 'ServerManager/FileandStorageServices' directory in server
fass_path = sm_path + 'FileandStorageServices/'


@app.route(fass_path)  # TODO redirect instead of route
@app.route(fass_path+'Servers')
def Servers_page():
    """the /ServerManager/FileandStorageServices/Servers page is the page of servers storages."""
    return Servers.load_page()


@app.route(fass_path+'Disks')
def Disks_page():
    """the /ServerManager/FileandStorageServices/Disks page is the page of servers disks."""
    return Disks.load_page()


@app.route(fass_path+'iSCSI')
def iSCSI_page():
    """the /ServerManager/FileandStorageServices/Disks page is the page of servers iSCSI."""
    return iSCSI.load_page()


@app.route(fass_path+'Shares')
def Shares_page():
    """the /ServerManager/FileandStorageServices/Shares page is the page of servers Shares."""
    return Shares.load_page()


@app.route(fass_path+'StoragePools')
def StoragePools_page():
    """the /ServerManager/FileandStorageServices/StoragePools page is the page of servers StoragePools."""
    return StoragePools.load_page()


@app.route(fass_path+'Volumes')
def Volumes_page():
    """the /ServerManager/FileandStorageServices/Volumes page is the page of servers Volumes."""
    return Volumes.load_page()


@app.route(fass_path+'WorkFolders')
def WorkFolders_page():
    """the /ServerManager/FileandStorageServices/WorkFolders page is the page of servers WorkFolders."""
    return WorkFolders.load_page()


if __name__ == '__main__':
    app.run()
