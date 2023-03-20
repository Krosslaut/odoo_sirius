odoo.define('bsi_birthday_reminder_on_attendance.greeting_message', function (require) {
"use strict";

var core = require('web.core');
var Widget = require('web.Widget');
var _t = core._t;
var GreetingMessage = require('hr_attendance.greeting_message');

var GreetingMessage = GreetingMessage.extend({
    template: 'HrAttendanceGreetingMessage',

    welcome_message: function() {
        var self = this;
        var now = this.attendance.check_in.clone();

        var employee_id = this.attendance.employee_id[0]
        this._rpc({
                    model: 'hr.employee',
                    method: 'get_todays_employees_birthday_list',
                    args: [employee_id, ],
                })
                .then(function (result) {
                    if (result) {
                        self.$('.o_hr_attendance_message_message').append(_t(result));
                    }
                });

        this.return_to_main_menu = setTimeout( function() { self.do_action(self.next_action, {clear_breadcrumbs: true}); }, 20000);
        if (now.hours() < 5) {
            this.$('.o_hr_attendance_message_message').append(_t("Good night"));
        } else if (now.hours() < 12) {
            if (now.hours() < 8 && Math.random() < 0.3) {
                if (Math.random() < 0.75) {
                    this.$('.o_hr_attendance_message_message').append(_t("The early bird catches the worm"));
                } else {
                    this.$('.o_hr_attendance_message_message').append(_t("First come, first served"));
                }
            } else {
                this.$('.o_hr_attendance_message_message').append(_t("Good morning"));
            }
        } else if (now.hours() < 17){
            this.$('.o_hr_attendance_message_message').append(_t("Good afternoon"));
        } else if (now.hours() < 23){
            this.$('.o_hr_attendance_message_message').append(_t("Good evening"));
        } else {
            this.$('.o_hr_attendance_message_message').append(_t("Good night"));
        }
        if(this.previous_attendance_change_date){
            var last_check_out_date = this.previous_attendance_change_date.clone();
            if(now - last_check_out_date > 24*7*60*60*1000){
                this.$('.o_hr_attendance_random_message').html(_t("Glad to have you back, it's been a while!"));
            } else {
                if(Math.random() < 0.02){
                    this.$('.o_hr_attendance_random_message').html(_t("If a job is worth doing, it is worth doing well!"));
                }
            }
        }
    },
});

core.action_registry.add('hr_attendance_greeting_message', GreetingMessage);
return GreetingMessage;

});
