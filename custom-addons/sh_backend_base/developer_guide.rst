How to use icons in other modules ?
------------------------------------------

1) Put sh_backend_base module in depends
2) if you want to add any icon for ex. sh-YouTube

Put this code in your module where you want to add icon

<span class="sh-YouTube"></span>

3) If you want to add dual tone icon for ex. sh-YouTube-dt
Note: All dual tone icon have -dt attached

Put this code in your module where you want to add icon

<span class="sh-YouTube-dt"><span class="path1"></span><span class="path2"></span></span>

4). If you want to send notification in bell icon

For eg:

Enable from res config setting first

class TestSale(models.Model):
    _inherit = 'sale.order'

    def write(self,vals):
        res = super(TestSale,self).write(vals)
        self.env['sh.user.push.notification'].create_user_notification(user=self.env.user,name="Hello there",description="What is your name",res_model="sale.order",res_id=self.id)
        return res

Check create_user_notification method for more details
