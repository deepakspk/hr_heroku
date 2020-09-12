from django.urls import path, re_path, reverse
from . import views
from django.contrib import admin

app_name = 'payroll'

urlpatterns = [
path('employee_list',views.EmployeeListView.as_view(),name='employee_list'),
path('table/',views.table,name='table'),

path('employee/<str:pk>/',views.EmployeeDetailView.as_view(),name='employee_detail'),
path('employee_create/',views.EmployeeCreateView.as_view(),name='employee_create'),
path('employee/update/<str:pk>/',views.EmployeeUpdateView.as_view(),name='employee_update'),
path('upload-employee-csv/', views.employee_upload, name="employee_upload"),
path('employee/delete/<str:pk>/',views.EmployeeDeleteView.as_view(),name='employee_delete'),

path('department_create/',views.DepartmentCreateView.as_view(),name='department_create'),
path('department_list',views.DepartmentListView.as_view(),name='department_list'),
path('department/<int:pk>/',views.DepartmentDetailView.as_view(),name='department_detail'),
path('department/update/<int:pk>/',views.DepartmentUpdateView.as_view(),name='department_update'),
path('department/delete/<int:pk>/',views.DepartmentDeleteView.as_view(),name='department_delete'),

path('payslip_list',views.PayslipListView.as_view(),name='payslip_list'),
path('payslip/<int:pk>/',views.PayslipDetailView.as_view(),name='payslip_detail'),
path('payslip_create/',views.PayslipCreateView.as_view(),name='payslip_create'),
path('payslip/update/<int:pk>/',views.PayslipUpdateView.as_view(),name='payslip_update'),
path('upload-payslip-csv/', views.paydetail_upload, name="paydetail_upload"),
path('upload-clinical-csv/', views.clinical_upload, name="clinical_upload"),
path('payslip/delete/<int:pk>/',views.PayslipDeleteView.as_view(),name='payslip_delete'),

path('additional_create/',views.AdditionalCreateView.as_view(),name='additional_create'),
path('additional_list',views.AdditionalListView.as_view(),name='additional_list'),
path('additional/<int:pk>/',views.AdditionalDetailView.as_view(),name='additional_detail'),
path('additional/update/<int:pk>/',views.AdditionalUpdateView.as_view(),name='additional_update'),
path('additional/delete/<int:pk>/',views.AdditionalDeleteView.as_view(),name='additional_delete'),
path('upload-additional_pay-csv/', views.additional_upload, name="additional_upload"),


path('deduction_create/',views.DeductionCreateView.as_view(),name='deduction_create'),
path('deduction_list',views.DeductionListView.as_view(),name='deduction_list'),
path('deduction/<int:pk>/',views.DeductionDetailView.as_view(),name='deduction_detail'),
path('deduction/update/<int:pk>/',views.DeductionUpdateView.as_view(),name='deduction_update'),
path('deduction/delete/<int:pk>/',views.DeductionDeleteView.as_view(),name='deduction_delete'),
path('upload-deduction_pay-csv/', views.deduction_upload, name="deduction_upload"),

path('process_salary/',views.ProcessSalaryListView.as_view(),name='process_salary_list'),
path('payroll_register/',views.PayrollRegisterView.as_view(),name='payroll_register'),
path('process_salary/<int:pk>/',views.ProcessSalaryDetailView.as_view(),name='process_salary_detail'),
path('process_salary_create/',views.ProcessSalaryCreateView.as_view(),name='process_salary_create'),
path('process_salary/update/<int:pk>/',views.ProcessSalaryUpdateView.as_view(),name='process_salary_update'),
path('process_salary/delete/<int:pk>/',views.ProcessSalaryDeleteView.as_view(),name='process_salary_delete'),

path('salary_report/',views.SalaryReport.as_view(),name='salary_report_list'),
path('report_detail/<int:pk>/',views.ReportDetailView.as_view(),name='report_detail'),
path('report_detail_view/<int:pk>/',views.ReportDetailView_Revised.as_view(),name='report_detail_view'),

path('thanks/', views.ThanksPage.as_view(), name="thanks"),

path('employee_payslip/<int:pk>/',views.EmployeePayslip,name='employee_payslip'),
path('salary_process_btn/<int:pk>/',views.update_ps, name='update_ps'),
path('empdeplist/<int:pk>/',views.ListofEmpInDep, name="empdeplist"),

path('payroll_list/',views.ListofPayroll, name="payroll_list"),
path('payroll_detail/<int:pk>/',views.DetailofPayroll, name="payroll_detail"),

path('payroll_report/<slug:payrollid>/<slug:empid>/',views.emppayslip,name='payroll_report'),
path('payroll_report_view/<slug:payrollid>/<slug:empid>',views.emppayslip_view,name='payroll_report_view'),

path('excle/<int:pk>',views.load_workbook, name="excle"),
path('bank_excle/<int:pk>',views.load_workbook_bank, name="bank_excle"),
path('lulu_excle/<int:pk>',views.load_workbook_lulu, name="lulu_excle"),

path ('pdf/<slug:pk>/<slug:empid>', views.payslipPdf, name='pdf'),
path ('pays_detail_pdf/<int:pk>/', views.PaysDetailsPDFView, name='pays_detail_pdf_list'),
path ('pay_detail_list_pdf', views.PayDetailListPDF, name='pay_detail_list_pdf'),
path ('PDFdeduction', views.DeductionsPDFView.as_view(), name='pdf_deduction'),
path ('PDFadditional', views.AdditionalPDFView.as_view(), name='pdf_additional'),

path ('salary_additional/<int:pk>/',views.SalaryAdditional, name="salary_additional"),
path ('salary_deductions/<int:pk>/',views.SalaryDeductions, name="salary_deductions"),
path ('employee_timesheet/<int:pk>/',views.EmpTimesheet, name="emp_timesheet"),

path ('timesheet_list/',views.EmployeeTimesheet.as_view(), name="timesheet_list"),
path('timesheet_create/',views.EmployeeTimesheetCreateView.as_view(),name='timesheet_create'),
path('timesheet/update/<int:pk>/',views.EmployeeTimesheetUpdateView.as_view(),name='timesheet_update'),
path('timesheet/delete/<int:pk>/',views.EmployeeTimesheetDeleteView.as_view(),name='timesheet_delete'),
path('upload-timesheet-csv/', views.timesheet_upload, name="timesheet_upload"),

path ('process_salary_additional/<int:pk>/',views.ProcessSalaryAdditional, name="process_salary_additional"),
path ('process_salary_deductions/<int:pk>/',views.ProcessSalaryDeductions, name="process_salary_deductions"),
path ('process_salary_timesheet/<int:pk>/',views.ProcessSalaryTimesheet, name="process_salary_timesheet"),
path ('process_salary_master/<int:pk>/',views.ProcessSalaryMaster, name="process_salary_master"),
path ('process_salary_paydetails/<int:pk>/',views.ProcessSalaryPayDetails, name="process_salary_paydetails"),
path ('process_salary_bank/<int:pk>/',views.ProcessSalaryBank, name="process_salary_bank"),
path ('process_salary_lulu/<int:pk>/',views.ProcessSalaryLulu, name="process_salary_lulu"),

path ('salary_record/', views.SalaryRecord, name='salary_record'),
path ('salary_record_detail/<slug:empid>', views.SalaryRecordDetail, name='salary_record_detail'),

path('emailpdf/<str:pk>/<str:empid>',views.singleEmail,name='emailpdf'),
path('email/<str:pk>/',views.email,name='email'),
path('downloadAll/<str:pk>/',views.downloadAll,name='downloadAll'),
path('displayPdf/<str:pk>/<str:empid>',views.DisplayPdf.as_view(),name='displayPdf'),

path('delete_all_timesheet/',views.delete_everything, name='delete_everything'),

path('hr_records/',views.hr_records, name='hr_records'),

path('labour_contract_list',views.LabourContractListView.as_view(),name='labour_contract_list'),
path('labour_contract_print',views.LabourContractPrint, name='labour_contract_print'),
path('labour_contract_detail/<str:pk>/',views.LabourContractDetailView.as_view(),name='labour_contract_detail'),
path('labour_contract_create/',views.LabourContractCreateView.as_view(),name='labour_contract_create'),
path('contract/update/<str:pk>/',views.LabourContractUpdateView.as_view(),name='contract_update'),
path('contract/delete/<str:pk>/',views.LabourContractDeleteView.as_view(),name='labour_contract_delete'),

path('work_permit_list',views.WorkPermitListView.as_view(),name='work_permit_list'),
path('work_permit_print',views.WorkPermitPrint, name='work_permit_print'),
path('work_permit_detail/<str:pk>/',views.WorkPermitDetailView.as_view(),name='work_permit_detail'),
path('work_permit/update/<str:pk>/',views.WorkPermitUpdateView.as_view(),name='work_permit_update'),
path('work_permit/delete/<str:pk>/',views.WorkPermitDeleteView.as_view(),name='work_permit_delete'),
path('work_permit_create/',views.WorkPermitCreateView.as_view(),name='work_permit_create'),

path('eid_collect_list',views.EidCollectListView.as_view(),name='eid_collect_list'),
path('eid_collect_print',views.EidCollectPrint, name='eid_collect_print'),
path('eid_collect_detail/<str:pk>/',views.EidCollectDetailView.as_view(),name='eid_collect_detail'),
path('eid_collect/update/<str:pk>/',views.EidCollectUpdateView.as_view(),name='eid_collect_update'),
path('eid_collect/delete/<str:pk>/',views.EidCollectDeleteView.as_view(),name='eid_collect_delete'),
path('eid_collect_create/',views.EidCollectCreateView.as_view(),name='eid_collect_create'),

path('new_eid_list',views.NewEidListView.as_view(),name='new_eid_list'),
path('new_eid_print',views.NewEidPrint, name='new_eid_print'),
path('new_eid_detail/<str:pk>/',views.NewEidDetailView.as_view(),name='new_eid_detail'),
path('new_eid/update/<str:pk>/',views.NewEidUpdateView.as_view(),name='new_eid_update'),
path('new_eid/delete/<str:pk>/',views.NewEidDeleteView.as_view(),name='new_eid_delete'),
path('new_eid_create/',views.NewEidCreateView.as_view(),name='new_eid_create'),

path('upload-New-EID-csv/', views.neweid_upload, name="neweid_upload"),
path('upload-labour-contract-csv/', views.labourcontract_upload, name="labour_contract_upload"),
path('update-labour-contract-csv/', views.passport_update, name="passport_update"),

path('p_contract_sign',views.p_contract_sign, name='p_contract_sign'),
path('p_wp_sign',views.p_wp_sign, name='p_wp_sign'),
path('p_eid_collect',views.p_eid_collect, name='p_eid_collect'),
path('p_p_collect',views.p_p_collect, name='p_p_collect'),


path('p_passport_collect',views.p_passport_collect, name='p_passport_collect'),
path('p_visa_medical',views.p_visa_medical, name='p_visa_medical'),

path('passport_return_list',views.PassportReturnListView.as_view(),name='p_return_list'),
path('p_return/update/<str:pk>/',views.PassportReturnUpdateView.as_view(),name='p_return_update'),

path('passport_return_print',views.PassportReturnPrint, name='p_return_print'),
path('update-employee-csv/', views.employee_update, name="employee_update"),
path('labour_contract_report',views.LabourContractReport, name='labour_contract_report'),

path('multiple_passport_return',views.multiple_passport_return, name='m_passport_return'),
path('m_passport_return_collected',views.multiple_passport_collect, name='m_passport_return_collected'),
path('labour_contract_create_multiple',views.labour_contract_create_multiple, name='m_labour_contract_create'),
path('new_EID_create_multiple',views.new_eid_create_multiple, name='m_new_eid_create'),
path('multiple_new_eid_update',views.multiple_new_eid_return, name='m_new_eid_update'),

path('employee_export',views.employee_export, name='employee_export'),

]
