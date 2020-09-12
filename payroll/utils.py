import datetime
from reportlab.platypus import Table
from reportlab.platypus import Image
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter, A4
from django.db.models import Sum, Avg, Max, Count, Min
from . import models
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Frame
from django.conf import settings
from reportlab.platypus import PageBreak

def getPdf(pk,empid):
    
    filepath = settings.MEDIA_ROOT + "/pdf/"
    fileName = filepath+empid+"__"+pk+".pdf"

    getEmp = models.Employee.objects.get(employee_id=empid)
    getReport = models.Report.objects.get(payroll_id=pk,employee_id=empid)
    payroll_month = getReport.payroll_month
    payroll_id = getReport.payroll_id

    addpay = models.Additionalpays.objects.filter(report=getReport)
    dedpay = models.Deductions.objects.filter(report=getReport)
    empAdd = models.Additionalpays.objects.filter(report=getReport).aggregate(Sum('amount'))['amount__sum']
    empDed = models.Deductions.objects.filter(report=getReport).aggregate(Sum('amount'))['amount__sum']
    timesheet = models.ReportTimesheet.objects.filter(report=getReport)
    lowp = (getReport.lowp_deduction) or 0

    basic_rate = (getReport.basic_salary)/timesheet[0].total
    allowance_rate = (getReport.housing_allowance)/timesheet[0].total
    transport_rate = (getReport.transportation_allowance)/timesheet[0].total
    other_rate = (getReport.other)/timesheet[0].total
    total_rate = basic_rate + allowance_rate  + transport_rate + other_rate

    normal_basic = basic_rate * timesheet[0].normal
    normal_allowance = allowance_rate * timesheet[0].normal
    normal_transport = transport_rate * timesheet[0].normal
    normal_other = other_rate * timesheet[0].normal
    normal_total = normal_basic + normal_allowance + normal_transport + normal_other

    weekend_basic = basic_rate * timesheet[0].weekend
    weekend_allowance = allowance_rate * timesheet[0].weekend
    weekend_transport = transport_rate * timesheet[0].weekend
    weekend_other = other_rate * timesheet[0].weekend
    weekend_total = weekend_basic + weekend_allowance + weekend_transport + weekend_other

    holiday_basic = basic_rate * timesheet[0].holiday
    holiday_allowance = allowance_rate * timesheet[0].holiday
    holiday_transport = transport_rate * timesheet[0].holiday
    holiday_other = other_rate * timesheet[0].holiday
    holiday_total = holiday_basic + holiday_allowance + holiday_transport + holiday_other

    vacation_basic = basic_rate * timesheet[0].vacation
    vacation_allowance = allowance_rate * timesheet[0].vacation
    vacation_transport = transport_rate * timesheet[0].vacation
    vacation_other = other_rate * timesheet[0].vacation
    vacation_total = vacation_basic + vacation_allowance + vacation_transport + vacation_other

    sick_basic = basic_rate * timesheet[0].sick
    sick_allowance = allowance_rate * timesheet[0].sick
    sick_transport = transport_rate * timesheet[0].sick
    sick_other = other_rate * timesheet[0].sick
    sick_total = sick_basic + sick_allowance + sick_transport + sick_other

    total_basic = normal_basic + weekend_basic + holiday_basic + vacation_basic + sick_basic
    total_allowance = normal_allowance + weekend_allowance + holiday_allowance + vacation_allowance + sick_allowance
    total_transport = normal_transport + weekend_transport + holiday_transport + vacation_transport + sick_transport
    total_other = normal_other + weekend_other + holiday_other + vacation_other + sick_other
    grand_total = total_basic + total_allowance + total_transport + total_other


    basic_rate = (round(basic_rate,2))
    allowance_rate = (round(allowance_rate,2))
    transport_rate = (round(transport_rate,2))
    other_rate = (round(other_rate,2))
    total_rate = (round(total_rate,2))

    normal_basic = (round(normal_basic,2))
    normal_allowance = (round(normal_allowance,2))
    normal_transport = (round(normal_transport,2))
    normal_other = (round(normal_other,2))
    normal_total = (round(normal_total,2))

    weekend_basic = (round(weekend_basic,2))
    weekend_allowance = (round(weekend_allowance,2))
    weekend_transport = (round(weekend_transport,2))
    weekend_other = (round(weekend_other,2))
    weekend_total = (round(weekend_total,2))

    holiday_basic = (round(holiday_basic,2))
    holiday_allowance = (round(holiday_allowance,2))
    holiday_transport = (round(holiday_transport,2))
    holiday_other = (round(holiday_other,2))
    holiday_total = (round(holiday_total,2))

    vacation_basic = (round(vacation_basic,2))
    vacation_allowance = (round(vacation_allowance,2))
    vacation_transport = (round(vacation_transport,2))
    vacation_other = (round(vacation_other,2))
    vacation_total = (round(vacation_total,2))

    sick_basic = (round(sick_basic,2))
    sick_allowance = (round(sick_allowance,2))
    sick_transport = (round(sick_transport,2))
    sick_other = (round(sick_other,2))
    sick_total = (round(sick_total,2))

    total_basic = (round(total_basic,2))
    total_allowance = (round(total_allowance,2))
    total_transport = (round(total_transport,2))
    total_other = (round(total_other,2))
    grand_total = (round(grand_total,2))


    empAddAmount = empAdd or 0
    empDedAmount = empDed or 0
    addamt = (round(empAddAmount,2))
    dedamt = (round(empDedAmount,2))
    dedamount = dedamt
    net = (grand_total + addamt) - dedamount
    yrsbasic = models.Report.objects.filter(
            employee_id=getReport.employee_id,
            payroll_month__lte=getReport.payroll_month
        ).aggregate(Sum('basic_salary'))['basic_salary__sum']

    yrshousing = models.Report.objects.filter(
            employee_id=getReport.employee_id,
            payroll_month__lte=getReport.payroll_month
        ).aggregate(Sum('housing_allowance'))['housing_allowance__sum']

    yrstransport = models.Report.objects.filter(
            employee_id=getReport.employee_id,
            payroll_month__lte=getReport.payroll_month
        ).aggregate(Sum('transportation_allowance'))['transportation_allowance__sum']

    yrsother = models.Report.objects.filter(
            employee_id=getReport.employee_id,
            payroll_month__lte=getReport.payroll_month
        ).aggregate(Sum('other'))['other__sum']

    yrslwop = models.Report.objects.filter(
            employee_id=getReport.employee_id,
            payroll_month__lte=getReport.payroll_month
        ).aggregate(Sum('lowp_deduction'))['lowp_deduction__sum']

    yrsGross = yrsbasic + yrshousing + yrstransport + yrsother - yrslwop
    yrsGross = (round(yrsGross,2))



    yrsAdd = models.Additionalpays.objects.filter(
            report__employee_id=getReport.employee_id,
            report__payroll_month__lte=getReport.payroll_month
        ).aggregate(Sum('amount'))['amount__sum']
    yearAdd = yrsAdd or 0
    yearAdd = (round(yearAdd,2))

    yrsDed = models.Deductions.objects.filter(
            report__employee_id=getReport.employee_id,
            report__payroll_month__lte=getReport.payroll_month
        ).aggregate(Sum('amount'))['amount__sum']

    yearDed = yrsDed or 0
    yrded = (round(yearDed,2))

    yrsNet = (yrsGross + yearAdd ) - yrded
    yearNet = yrsNet or 0
    yearNet = (round(yearNet,2))

    pdf = SimpleDocTemplate(fileName, pagesize=A4, 
        rightMargin=.3*inch,
        leftMargin=.3*inch,
        topMargin=.3*inch, 
        bottomMargin=.3*inch,)
    
    elems = []

    picture = Image('static/images/aspen.png')
    picture.drawWidth = 200
    picture.drawHeight = 35
    pic = Table([[picture]],200,35)

    pic = Table([
        [pic]
    ],[500])
    picStyle = TableStyle([
        ('BOTTOMPADDING',(0,0),(-1,-1), 5),
    ])
    pic.setStyle(picStyle)
    elems.append(pic)

    location = Table([
        ['ABU DHABI, UAE']
    ], [500])
    locationStyle = TableStyle([
        ('BOTTOMPADDING',(0,0),(-1,-1), 10),
    ])
    location.setStyle(locationStyle)
    elems.append(location)

    payslip = Table([
        ['PAYSLIP']
    ], [500])
    payslipStyle = TableStyle([
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
        ('LINEABOVE',(0,0),(-1,-1),1,colors.ReportLabBlue),
        ('TOPPADDING',(0,0),(-1,-1), 5),
        ('BOTTOMPADDING',(0,0),(-1,-1), 0),
    ])
    payslip.setStyle(payslipStyle)
    elems.append(payslip)

    month = Table([
        [f"For the Month of {payroll_month}"]
    ], [500])
    monthStyle = TableStyle([
        ('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('TOPPADDING',(0,0),(-1,-1), 0),
        ('BOTTOMPADDING',(0,0),(-1,-1), 20),
    ])
    month.setStyle(monthStyle)
    elems.append(month)

    name = Table([
        ['Employee Name','', getEmp.full_name]
    ], [100,10,410])
    nameStyle = TableStyle([
        ('ALIGN',(0,0),(-1,-1),'LEFT'),
        ('FONTSIZE', (1,0), (-1,0), 13),
        ('VALIGN',(0,0),(-1,0),'TOP'),
        ('FONTNAME', (0,0), (-1,-1),
            'Helvetica-Bold'
            ),
        ('TOPPADDING',(0,0),(-1,-1), 0),
        ('BOTTOMPADDING',(0,0),(-1,-1), 0),
    ])
    name.setStyle(nameStyle)
    elems.append(name)

    permit = Table([
        ['Work Permit','', getReport.work_permit]
    ], [100,10,410])    
    permitStyle = TableStyle([
        ('TOPPADDING',(0,0),(-1,-1), 5),
        ('BOTTOMPADDING',(0,0),(-1,-1), 0),
    ])
    permit.setStyle(permitStyle)
    elems.append(permit)

    mode = Table([
        ['Mode of payment',' ', getReport.mode_of_payment]
    ], [100,10,410])
    modeStyle = TableStyle([
        ('TOPPADDING',(0,0),(-1,-1), 0),
        ('BOTTOMPADDING',(0,0),(-1,-1), 30),
    ])
    mode.setStyle(modeStyle)
    elems.append(mode)

    heading = Table([
        ['','Days','Basic','Allowances','Transportation','Other','Total']
    ], [140,60,60,60,80,60,60])
    headingStyle = TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
    ])
    heading.setStyle(headingStyle)
    elems.append(heading)

    ##salray table starts
    salary = Table([
        ['Salary',':','',getReport.basic_salary,getReport.housing_allowance,getReport.transportation_allowance,getReport.other,getReport.gross_pay]
    ], [100,40,60,60,80,60,60])

    rate = Table([
        ['Rate',':','',basic_rate,allowance_rate,transport_rate,other_rate,total_rate]
    ], [100,40,60,60,80,60,60])


    normal = Table([
        ['Normal',':',timesheet[0].normal,normal_basic,normal_allowance,normal_transport,normal_other,normal_total]
    ], [100,40,60,60,80,60,60,60])

    weekend = Table([
        ['Weekend',':',timesheet[0].weekend,weekend_basic,weekend_allowance,weekend_transport,weekend_other,weekend_total]
    ], [100,40,60,60,80,60,60,60])

    holiday = Table([
        ['Holiday',':',timesheet[0].holiday,holiday_basic,holiday_allowance,holiday_transport,holiday_other,holiday_total]
    ], [100,40,60,60,80,60,60,60])

    vacation = Table([
        ['Vacation',':',timesheet[0].vacation,vacation_basic,vacation_allowance,vacation_transport,vacation_other,vacation_total]
    ], [100,40,60,60,80,60,60,60])

    sick = Table([
        ['Sick-Leave',':', timesheet[0].sick,sick_basic,sick_allowance,sick_transport,sick_other,sick_total]
    ], [100,40,60,60,80,60,60,60])

    lwop = Table([
        ['LWOP',':',timesheet[0].lwop,'-','-','-','-','-']
    ], [100,40,60,60,80,60,60,60])

    np = Table([
        ['N.P Days',':','0','-','-','-','-','-']
    ], [100,40,60,60,80,60,60,60])

    total = Table([
        ['Total',':',timesheet[0].total,total_basic,total_allowance,total_transport,total_other,grand_total]
    ], [100,40,60,60,80,60,60,60])
    totalStyle = TableStyle([
        ('BOTTOMPADDING',(0,0),(-1,-1), 10),
    ])
    total.setStyle(totalStyle)

    gross = Table([
        ['Gross Pay',':',grand_total]
    ], [120,40,350])
    grossStyle = TableStyle([
        ('BACKGROUND', (0,0),(8,0), colors.gray),
        ('TEXTCOLOR', (0,0),(-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0),(-1,0), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 5),
    ])
    gross.setStyle(grossStyle)

    salaryTable = [
        salary,
        rate,
        normal,
        weekend,
        holiday,
        vacation,
        sick,
        lwop,
        np,
        total,
        gross
    ]

    elems.extend(salaryTable)
    ### ends

    ### add pay
    if addpay:
        add = Table([
            ['Additional Pay']
        ], [520])
       
        newAdd = []
        for additional in addpay:
            col = [additional.additional,':',additional.amount]
            newAdd.append(col)
        add_item = Table(newAdd, [120,40,350],repeatRows=1)
        total_add = Table([
            ['TOTAL ADDITIONAL',':',addamt]
        ], [120,40,350])
        addStyle = TableStyle([
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ])
        add.setStyle(addStyle)
        total_addStyle = TableStyle([
                ('BACKGROUND', (0,0),(5,0), colors.lightgrey),
                ('FONTNAME', (0,0),(-1,0), 'Courier-Bold'),
                ('FONTSIZE', (0,0), (-1,0), 12),
                ('BOTTOMPADDING', (0,0), (-1,0), 5),
            ])
        total_add.setStyle(total_addStyle)
        addData = [add,add_item,total_add]
        elems.extend(addData)

    if dedpay:
        ded = Table([
            ['Deductions']
        ], [520])

        newDed = []        
        for deduction in dedpay:
            col2 = [deduction.deduction,':',deduction.amount]
            newDed.append(col2)
        ded_item = Table(newDed, [120,40,350],repeatRows=1)
        total_ded = Table([
            ['TOTAL DEDUCTION',':',dedamt]
        ], [120,40,350])
        dedStyle = TableStyle([
                ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ])
        ded.setStyle(dedStyle)
        total_dedStyle = TableStyle([
                ('BACKGROUND', (0,0),(5,0), colors.lightgrey),
                ('FONTNAME', (0,0),(-1,0), 'Courier-Bold'),
                ('FONTSIZE', (0,0), (-1,0), 12),
                ('BOTTOMPADDING', (0,0), (-1,0),5),
            ])
        total_ded.setStyle(total_dedStyle)
        dedData = [ded,ded_item,total_ded]
        elems.extend(dedData)

    ##net table 
    net = Table([
    ['NET PAY',':', net]
    ], [120,40,350])
    netStyle = TableStyle([
        ('BACKGROUND', (0,0),(5,0), colors.gray),
        ('TEXTCOLOR', (0,0),(-1,0), colors.whitesmoke),
        ('FONTNAME', (0,0),(-1,0), 'Courier-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 5),
    ])
    net.setStyle(netStyle)

    year_to = Table([
        ['YEAR-TO-DATE (Feb 2020 - Jan 2021)']
    ], [520])

    yr_gross = Table([
        ['YTD Gross Pay',':',yrsGross]
    ], [120,40,350])

    yr_add = Table([
        ['YTD Additional Pay',':',yearAdd ]
    ], [120,40,350])

    yr_ded = Table([
        ['YTD Deduction',':',yrded]
    ], [120,40,350])

    yr_net = Table([
        ['YTD Net Pay',':',yearNet]
    ], [120,40,350])
    year_toStyle = TableStyle([
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
    ])
    year_to.setStyle(year_toStyle)

    botTable = [net, year_to, yr_gross, yr_add, yr_ded, yr_net]
    elems.extend(botTable)

    pdf.build(elems)