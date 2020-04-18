# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class KeyPermissions(str, Enum):

    encrypt = "encrypt"
    decrypt = "decrypt"
    wrap_key = "wrapKey"
    unwrap_key = "unwrapKey"
    sign = "sign"
    verify = "verify"
    get = "get"
    list = "list"
    create = "create"
    update = "update"
    import_enum = "import"
    delete = "delete"
    backup = "backup"
    restore = "restore"
    recover = "recover"
    purge = "purge"

class SecretPermissions(str, Enum):

    get = "get"
    list = "list"
    set = "set"
    delete = "delete"
    backup = "backup"
    restore = "restore"
    recover = "recover"
    purge = "purge"

class CertificatePermissions(str, Enum):

    get = "get"
    list = "list"
    delete = "delete"
    create = "create"
    import_enum = "import"
    update = "update"
    managecontacts = "managecontacts"
    getissuers = "getissuers"
    listissuers = "listissuers"
    setissuers = "setissuers"
    deleteissuers = "deleteissuers"
    manageissuers = "manageissuers"
    recover = "recover"
    purge = "purge"

class StoragePermissions(str, Enum):

    get = "get"
    list = "list"
    delete = "delete"
    set = "set"
    update = "update"
    regeneratekey = "regeneratekey"
    recover = "recover"
    purge = "purge"
    backup = "backup"
    restore = "restore"
    setsas = "setsas"
    listsas = "listsas"
    getsas = "getsas"
    deletesas = "deletesas"

class SkuName(str, Enum):
    """SKU name to specify whether the key vault is a standard vault or a premium vault.
    """

    standard = "standard"
    premium = "premium"

class CreateMode(str, Enum):
    """The vault's create mode to indicate whether the vault need to be recovered or not.
    """

    recover = "recover"
    default = "default"

class Reason(str, Enum):
    """The reason that a vault name could not be used. The Reason element is only returned if
    NameAvailable is false.
    """

    account_name_invalid = "AccountNameInvalid"
    already_exists = "AlreadyExists"

class AccessPolicyUpdateKind(str, Enum):

    add = "add"
    replace = "replace"
    remove = "remove"
