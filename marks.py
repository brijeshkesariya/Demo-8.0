from openerp.osv import fields, osv



class student_details(osv.osv):
	_name = 'student.details'
	_columns = {
		'stu_name': fields.many2one('student.student','Student Name'),		
		'mark_ids':fields.one2many('student.marks','student_mark_ids','Marks'),   ###The Reference Id Which Referes the Marks Class
		}
student_details()

class student_marks(osv.osv):

    _name = "student.marks"
    _description = "Marks Records"
    _columns = {
	       'student_mark_ids':fields.many2one('student.student','Student Ref'),   ###The Reference Of Above Student Details Class
	       'subject': fields.char('Subject'),
	       'achv':fields.integer('Achieved'),
	       'from': fields.integer('From'),
	       }
student_marks()


