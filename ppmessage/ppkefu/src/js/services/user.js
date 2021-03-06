ppmessageModule.factory('yvUser', [
    "yvSys",
    "yvConstants",
function (yvSys, yvConstants) {
    var user = {
        id: null,
        icon: null,
        name: null,
        uuid: null,
        email: null,
        fullname: null,
        signature: null,
        device_uuid: null,
        updatetime: null,
        is_online: false,
        access_token: null,
        password: null,
        status: yvConstants.USER_STATUS.READY,
        
        app: {
            uuid: "",
            app_key: "",
            app_name: "",
            app_secret: ""
        },

        show_badge: null,
        mute_notification: null,
        silence_notification: null,
        mute_other_mobile_device: null,

        android_notification_type: yvConstants.NOTIFICATION_TYPE.GCM        
    };

    // update user from API/PP_GET_USER_INFO
    function _update_user_from_api(data) {
        user.uuid = data.uuid;
        user.icon = data.user_icon;
        user.name = data.user_name;
        user.email = data.user_email;
        user.fullname = data.user_fullname;
        user.signature = data.user_signature;
        user.updatetime = data.updatetime;
        user.is_online = true;
        user.device_uuid = data.ppkefu_browser_device_uuid;
                       
        return user;
    }

    // update user from API return
    function _update_user_from_login(data) {
        
        user.app = data.app;
        user.uuid = data.uuid;
        user.icon = data.user_icon;
        user.name = data.user_name;
        user.email = data.user_email;
        user.fullname = data.user_fullname;
        user.signature = data.user_signature;
        user.updatetime = data.updatetime;
        user.password = data.user_password;
        user.is_online = true;
        user.status = yvConstants.USER_STATUS.READY;
        user.device_uuid = data.ppkefu_browser_device_uuid;
        
        return user;
    }

    function _update_user_from_db(item) {
        user.id = item.id;
        user.uuid = item.user_uuid;
        user.is_online = !!item.is_online;
        user.device_uuid = item.device_uuid;
        user.access_token = item.access_token;
        
        user.app = {
            uuid: item.app_uuid,
            app_key: item.app_key,
            app_name: item.app_name,
            app_secret: item.app_secret
        };

        user.show_badge = !!item.show_badge;
        user.mute_notification = !!item.mute_notification;
        user.silence_notification = !!item.silence_notification;

        user.android_notification_type = item.android_notification_type || yvConstants.NOTIFICATION_TYPE.GCM;
        return user;
    }
    
    return {
        update_user_from_login: function (_user) {
            return _update_user_from_login(_user);
        },

        update_user_from_api: function (_data) {
            return _update_user_from_api(_data);
        },

        update_user_from_db: function (item) {
            return _update_user_from_db(item);
        },

        set: function (attribute, value) {
            if (user.hasOwnProperty(attribute)) {
                user[attribute] = value;
            }
        },

        mset: function (data) {
            angular.forEach(data, function (value, key) {
                if (user.hasOwnProperty(key)) {
                    user[key] = value;
                }
            });
        },

        get: function (attribute) {
            if (arguments.length === 0) {
                return user;
            }
            if (user.hasOwnProperty(attribute)) {
                return user[attribute];
            }
            return null;
        },
    };
}]);
