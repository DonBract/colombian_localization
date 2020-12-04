import frappe
from erpnext.selling.doctype.customer.customer import Customer

def validation(self):
    self.flags.is_new_doc = self.is_new()
    self.flags.old_lead = self.lead_name
    validate_party_accounts(self)
    self.validate_credit_limit_on_change()
    self.set_loyalty_program()
    self.check_customer_group_change()
    self.validate_default_bank_account()

    # set loyalty program tier
    if frappe.db.exists('Customer', self.name):
        customer = frappe.get_doc('Customer', self.name)
        if self.loyalty_program == customer.loyalty_program and not self.loyalty_program_tier:
            self.loyalty_program_tier = customer.loyalty_program_tier

    if self.sales_team:
        if sum([member.allocated_percentage or 0 for member in self.sales_team]) != 100:
            frappe.throw(_("Total contribution percentage should be equal to 100"))
    
    if self.country == 'Colombia':
        multiplication_factors = [71, 67, 59, 53, 47, 43, 41, 37, 29, 23, 19, 17, 13, 7, 3]
        if not len(self.vat) <= len(multiplication_factors):
            frappe.throw(_("Error en la validacion del vat"))

Customer.validation = validation