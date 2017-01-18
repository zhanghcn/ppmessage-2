# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com
# All rights reserved
#

from ppmessage.core.constant import enum

API_ERR = enum("NO_ERR",
               "NO_JSON",
               "NO_UUID",
               "NO_ACCESS_TOKEN",
               "WRONG_ACCESS_TOKEN",
               "NO_VALID",
               "NO_PARA",
               "NO_USER",
               "NO_DEVICE",
               "NO_ENT",
               "MIS_ERR",
               "NO_TASK",
               "NO_PUSH",
               "NO_APP",
               "NO_FILE",
               "NO_MATERIAL",
               "MESSAGE",
               "SYS_ERR",
               "NO_OBJECT",
               "ERR_SIG",
               "NO_PERM",
               "NO_ACTION",
               "EX_USER",
               "NO_LEADER",
               "ERROR_VERIFY_CODE",
               "EX_DEVICE",
               "NO_CONVERSATION",
               "EX_CONTACT",
               "WRONG_PARA",
               "NOT_PORTAL",
               "NO_ORG_GROUP",
               "NOT_LIST",
               "NOT_GROUP_USER",
               "GENERIC_UPDATE",
               "NO_SERVICE_USER",
               "NO_CONVERSATION_MEMBER",
               "CONVERSATION_TYPE",
               "EX_GROUP_USER",
               "APP_OWNER",
               "NOT_OWNER",
               "NO_APP_USER",
               "PAGE_TOO_LARGE",
               "PAGE_MAX_MIN",
               "NOT_ADMIN",
               "INVALID_PARA",
               "NO_TABLE",
               "INVALID_PHONENUMBER"
               )

API_ERR_DESC = {
    API_ERR.NO_ERR: "success.",
    API_ERR.NO_JSON: "request not json.",
    API_ERR.NO_UUID: "no required UUIDs.",
    API_ERR.NO_ACCESS_TOKEN: "no such access token.",
    API_ERR.WRONG_ACCESS_TOKEN: "wrong access token.",
    API_ERR.NO_VALID: "session timeout or already logout.",
    API_ERR.NO_PARA: "required parameter not provided.",
    API_ERR.NO_USER: "no such user",
    API_ERR.NO_DEVICE: "no such device",
    API_ERR.NO_ENT: "no such enterprise user",
    API_ERR.MIS_ERR: "password mismatch.",
    API_ERR.NO_TASK: "no such push task.",
    API_ERR.NO_PUSH: "no such push item.",
    API_ERR.NO_APP: "no such application.",
    API_ERR.NO_FILE: "no such file.",
    API_ERR.NO_MATERIAL: "no such material.",
    API_ERR.MESSAGE: "illegal message.",
    API_ERR.SYS_ERR: "system error.",
    API_ERR.NO_OBJECT: "no such object",
    API_ERR.ERR_SIG: "wrong signal.",
    API_ERR.NO_PERM: "no such permission.",
    API_ERR.NO_ACTION: "no such action.",
    API_ERR.EX_USER: "user already exited.",
    API_ERR.NO_LEADER: "group has no leader so far.",
    API_ERR.ERROR_VERIFY_CODE: "verify code error.",
    API_ERR.NO_CONVERSATION: "no such conversation",
    API_ERR.EX_CONTACT: "contact existed.",
    API_ERR.EX_DEVICE: "device existed.",
    API_ERR.WRONG_PARA: "wrong type of para.",
    API_ERR.NOT_PORTAL: "not portal user of PPMESSAGE.",
    API_ERR.NO_ORG_GROUP: "no such org group.",
    API_ERR.NOT_LIST: "parameter is not a list, but list is required.",
    API_ERR.NOT_GROUP_USER: "user not in this group",
    API_ERR.GENERIC_UPDATE: "can not update",
    API_ERR.NO_SERVICE_USER: "no service user for the portal user.",
    API_ERR.NO_CONVERSATION_MEMBER: "no conversation member.",
    API_ERR.CONVERSATION_TYPE: "wrong conversation type.",
    API_ERR.EX_GROUP_USER: "group user has been in this covnersation.",
    API_ERR.APP_OWNER: "user is the owner of app.",
    API_ERR.NOT_OWNER: "user is not the owner of app.",
    API_ERR.NO_APP_USER: "app not has this user.",
    API_ERR.PAGE_TOO_LARGE: "page offset is too large.",
    API_ERR.PAGE_MAX_MIN: "should not provide max_uuid and min_uuid in the same time.",
    API_ERR.NOT_ADMIN: "user is not a admin user.",
    API_ERR.INVALID_PARA: "invalid value of para.",
    API_ERR.NO_TABLE: "no such table",
    API_ERR.INVALID_PHONENUMBER: "Invalid phonenumber"
}

def getErrorDesc(code):
    _desc = API_ERR_DESC.get(code)
    if _desc == None:
        return "no such error"
    return _desc

