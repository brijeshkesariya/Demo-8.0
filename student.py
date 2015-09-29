from openerp.osv import fields, osv

import student 

class student_student(osv.Model):
	_name = 'student.student'
	_rec_name = 'stu_name'
	_columns = {
		
		'stu_name': fields.char('Student Name',size=64),
		'details': fields.text('Details'),
		'acad_id': fields.one2many('student.academic','student_ids','Academic'),    
		###'student_ids' field must be present in 'student.academic' table
		'date_of_birth':fields.date('Date Of Birth'),
		'image':fields.binary('Photo'),
		'validate':fields.boolean('Validate?',store=True, help="Shows If the Mobile No is Valid or Not."),
		####### compute='_compute_reconciled', readonly=True
		'mob':fields.integer('Mobile No.'),
		'age':fields.integer('Age.'),
		'weight':fields.integer('Weight.'),
		'height':fields.integer('Height.'),
		'tag_ids': fields.many2many('student.std', # other model name
			'std_rel', # new tabel name
			'student_id', # field 1 of std_rel table
			'std_id', # field 2 of std_rel table
			'Standrads'), # label
		'state':fields.selection((('draft','Draft'),('pending','Pending'),('done','Done')),'Status'),

		}

		

	def action_draft(self, cr, uid, ids, context=None):
		print "**********************************Hello Draft*********************************"
		self.write(cr,uid,ids,{'state':'draft'},context=None)
		return True

	def action_check_validate(self, cr, uid, ids, context=None):
		print "**********************************Hello Validate******************************"
		self.write(cr,uid,ids,{'state':'pending'},context=None)
		return True
		
	def action_confirm(self, cr, uid, ids, context=None):
		print "**********************************Hello Confirm*******************************"
		self.write(cr,uid,ids,{'state':'done'},context=None)
		return True
student_student()

class student_academic(osv.Model):

    _name = "student.academic"
    _description = "Academic Records"
    _columns = {
	       'student_ids':fields.many2one('student.student','Academic Ref'),
	       'school':fields.char('School',size=64, required=True),
	       'percentage':fields.char('Percentage',size=64),
	       }
student_academic()

class student_std(osv.Model):

	_name = 'student.std'
	_columns = {
		'name': fields.char('Standrads', size = 64, required = True),
		}
student_std()


