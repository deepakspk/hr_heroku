$("#astart_date0").hide()
$("#aend_date0").hide()
$("#dstart_date0").hide()
$("#dend_date0").hide()
function selectChange(id,value) {
 getid = id.match(/\d+/)[0]
 if(value !=="Monthly"){
   $("#dstart_date"+getid).hide()
   $("#dend_date"+getid).hide()
 } else{
   $("#dstart_date"+getid).show()
   $("#dend_date"+getid).show()
 }
}
function selectAddChange(id,value) {
 getid = id.match(/\d+/)[0]
 if(value !=="Monthly"){
   $("#astart_date"+getid).hide()
   $("#aend_date"+getid).hide()
 } else{
   $("#astart_date"+getid).show()
   $("#aend_date"+getid).show()
 }
}
var next = 0;
$("#add-more-pay").click(function(e) {
      e.preventDefault();
  var addto = "#field" + next;
  var addRemove = "#field" + (next);
  next = next + 1;
  var newIn = ' <div id="field' + next + '" name="field' + next +
    '"><div class="form-row">' +
    '<div class="form-group col-md-3">' +
    '<label for="additional_pay">Pay Type</label>' +
    '<select id="add_pay" class="form-control" name="apay_type'+next+'">' +
    '<option selected>Select Additional Pay</option>' +
    '<option>Annual Air ticket</option>' +
    '<option>Expense Reimbursement</option>' +
    '<option>Bonus</option>' +
    '<option>Other</option>' +
    '</select>' +
    '</div>' +
    '<div class="form-group col-md-2">' +
    '<label for="label">Label</label>' +
    '<input type="text" class="form-control" name="alabel'+next+'">' +
    '</div>' +

    '<div class="form-group col-md-1">' +
    '<label for="amount">Amount</label>' +
    '<input type="text" class="form-control" name="aamount'+next+'">' +
    '</div>' +
    '<div class="form-group col-md-2">' +
    '<label for="occurs">Occurs</label>' +
    '<select class="form-control" name="aoccurs'+next+'" id="aoccurs'+next+'" onchange="selectAddChange(this.id,this.value)">' +
    '<option >Once</option>' +
    '<option selected>Monthly</option>' +
    '</select>' +
    '</div>' +
    '<div class="form-group col-md-2" id="astart_date'+next+'">' +
      '<label>Start Date:</label>' +
      '<input type="date" name="astart_date'+next+'" class="form-control">' +
    '</div>' +
    '<div class="form-group col-md-2" id="aend_date'+next+'">' +
      '<label>End Date:</label>' +
      '<input type="date" class="form-control" name="aend_date'+next+'">' +
    '</div>' +
    '</div>';
  var newInput = $(newIn);
  var removeBtn = '<button id="remove' + (next - 1) + '" class="btn btn-danger remove-me" >Remove</button></div></div><div id="field">';
  var removeButton = $(removeBtn);
  $(addto).after(newInput);
  $(addRemove).after(removeButton);
  $("#field" + next).attr('data-source', $(addto).attr('data-source'));
  $("#count").val(next);

  $('.remove-me').click(function(e) {
    e.preventDefault();
    var fieldNum = this.id.charAt(this.id.length - 1);
    var fieldID = "#field" + fieldNum;
    $(this).remove();
    $(fieldID).remove();
  });
});

var next1 = 0;
$("#deduct-more-pay").click(function(e) {
  e.preventDefault();
  var addto = "#fielded" + next1;
  var addRemove = "#fielded" + (next1);
  next1 = next1 + 1;
  var newIn = '<div id="fielded' + next1 + '" name="fielded' + next1 +
    '"><div class="form-row">' +
    '<div class="form-group col-md-3">' +
    '<label for="additional_pay">Deduction Type</label>' +
    '<select id="add_pay" class="form-control" name="dpay_type'+next1+'" >' +
    '<option selected>Select Deduction</option>' +
    '<option>Housing Loan</option>' +
    '<option>Salary Advance</option>' +
    '<option>Loan</option>' +
    '<option>Other</option>' +
    '</select>' +
    '</div>' +
    '<div class="form-group col-md-2">' +
    '<label for="label">Label</label>' +
    '<input type="text" class="form-control" name="dpay_label'+next1+'">' +
    '</div>' +

    '<div class="form-group col-md-1">' +
    '<label for="amount">Amount</label>' +
    '<input type="text" class="form-control" name="dpay_amount'+next1+'">' +
    '</div>' +
    '<div class="form-group col-md-2">' +
    '<label for="occurs">Occurs</label>' +
    '<select class="form-control" name="dpay_occur'+next1+'" id="doccurs' + next1 + '" onchange=selectChange(this.id,this.value)>' +
    '<option>Once</option>' +
    '<option selected>Monthly</option>' +
    '</select>' +
    '</div>' +
    '<div class="form-group col-md-2" id="dstart_date' + next1 + ' name="dpay_start'+next1+'">' +
    '<label>Start Date:</label>' +
    '<input type="date" class="form-control">' +
    '</div>' +
    '<div class="form-group col-md-2" id="dend_date' + next1 + ' name="dpay_end'+next1+'">' +
    '<label>End Date:</label>' +
    '<input type="date" class="form-control">' +
    '</div>' +
    '</div>';
  var newInput = $(newIn);
  var removeBtn = '<button id="remove' + (next1 - 1) + '" class="btn btn-danger remove-me" >Remove</button></div></div><div id="fielded">';
  var removeButton = $(removeBtn);
  $(addto).after(newInput);
  $(addRemove).after(removeButton);
  $("#fielded" + next1).attr('data-source', $(addto).attr('data-source'));
  $("#count").val(next1);

  $('.remove-me').click(function(e) {
    e.preventDefault();
    var fieldNum = this.id.charAt(this.id.length - 1);
    var fieldID = "#fielded" + fieldNum;
    $(this).remove();
    $(fieldID).remove();
  });
});
