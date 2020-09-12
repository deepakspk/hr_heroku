$(document).ready(function () {
    $("#astart_date0").hide();
    $("#aend_date0").hide();
    $("#dstart_date0").hide();
    $("#dend_date0").hide();
    var counter = 1;

    $("#addrow").on("click", function (e) {
      e.preventDefault();
        var newRow = $("<tr>");
        var cols = "";

        cols += '<div class="form-row" id="addPay'+counter+'">' +
    '<div class="form-group col-md-3">' +
    '<label for="additional_pay">Pay Type</label>' +
    '<select id="add_pay" class="form-control" name="apay_type' +
    counter +
    '">' +
    "<option selected>Select Additional Pay</option>" +
    "<option>Annual Air ticket</option>" +
    "<option>Expense Reimbursement</option>" +
    "<option>Advance Salary</option>" +
    "<option>Bonus</option>" +
    "<option>Other</option>" +
    "</select>" +
    "</div>" +
    '<div class="form-group col-md-2">' +
    '<label for="label">Label</label>' +
    '<input type="text" class="form-control" name="alabel' +
    counter +
    '">' +
    "</div>" +
    '<div class="form-group col-md-1">' +
    '<label for="amount">Amount</label>' +
    '<input type="text" class="form-control" name="aamount' +
    counter +
    '">' +
    "</div>" +
    '<div class="form-group col-md-1">' +
    '<label for="occurs">Occurs</label>' +
    '<select class="form-control" name="aoccurs' +
    counter +
    '" id="aoccurs' +
    counter +
    '" onchange="selectAddChange(this.id,this.value)">' +
    "<option >Once</option>" +
    "<option selected>Monthly</option>" +
    "</select>" +
    "</div>" +
    '<div class="form-group col-md-2" id="astart_date' +
    counter +
    '">' +
    "<label>Start Date:</label>" +
    '<input type="date" name="astart_date' +
    counter +
    '" class="form-control">' +
    "</div>" +
    '<div class="form-group col-md-2" id="aend_date' +
    counter +
    '">' +
    "<label>End Date:</label>" +
    '<input type="date" class="form-control" name="aend_date' +
    counter +
    '">' +
    "</div>" +
    '<div class="form-group col-md-1 mt-4"  >'+
        '<button class="btn btn-md btn-danger" style="margin-top:8px" id="addBtn'+counter+'" onclick ="removeAdd(this.id)">Delete</button>'+
    '</div>'+
    "</div>";
        cols += '';
        newRow.append(cols);
        $(".add-pay-list").append(newRow);
        counter++;
    });


    dcounter=1;
    $("#addDrow").on("click", function (e) {
      e.preventDefault();
        var newRow = $("<tr>");
        var cols = "";

        cols += '<div class="form-row" id="dedPay'+dcounter+'">' +
    '<div class="form-group col-md-3">' +
    '<label for="additional_pay">Deduction Type</label>' +
    '<select id="add_pay" class="form-control" name="dpay_type' +
    dcounter +
    '" >' +
    "<option selected>Select Deduction</option>" +
    "<option>Housing Loan</option>" +
    "<option>Salary Advance</option>" +
    "<option>Traffic Fine</option>" +
    "<option>Loan</option>" +
    "<option>Other</option>" +
    "</select>" +
    "</div>" +
    '<div class="form-group col-md-2">' +
    '<label for="label">Label</label>' +
    '<input type="text" class="form-control" name="dpay_label' +
    dcounter +
    '">' +
    "</div>" +
    '<div class="form-group col-md-1">' +
    '<label for="amount">Amount</label>' +
    '<input type="text" class="form-control" name="dpay_amount' +
    dcounter +
    '">' +
    "</div>" +
    '<div class="form-group col-md-1">' +
    '<label for="occurs">Occurs</label>' +
    '<select class="form-control" name="dpay_occur' +
    dcounter +
    '" id="doccurs' +
    dcounter +
    '" onchange=selectChange(this.id,this.value)>' +
    "<option>Once</option>" +
    "<option selected>Monthly</option>" +
    "</select>" +
    "</div>" +
    '<div class="form-group col-md-2" id="dstart_date' +
    dcounter +
    '" name="dpay_start' +
    dcounter +
    '">' +
    "<label>Start Date:</label>" +
    '<input type="date" class="form-control">' +
    "</div>" +
    '<div class="form-group col-md-2" id="dend_date' +
    dcounter +
    '" name="dpay_end' +
    dcounter +
    '">' +
    "<label>End Date:</label>" +
    '<input type="date" class="form-control">' +
    "</div>" +
    '<div class="form-group col-md-1 mt-4"  >'+
        '<button class="btn btn-md btn-danger" style="margin-top:8px" id="addBtn'+dcounter+'" onclick ="removeDed(this.id)">Delete</button>'+
    '</div>'+
    '</div>';
        newRow.append(cols);
        $(".ded-pay-list").append(newRow);
        dcounter++;
    });

});

function removeAdd(id){
        getid = id.match(/\d+/)[0];
        var field = '#addPay'+getid
        $(field).remove();
    }
    function removeDed(id){
        getid = id.match(/\d+/)[0];
        var field = '#dedPay'+getid
        $(field).remove();
    }

function selectAddChange(id, value) {
  getid = id.match(/\d+/)[0];
  if (value !== "Monthly") {
    $("#astart_date" + getid).hide();
    $("#aend_date" + getid).hide();
  } else {
    $("#astart_date" + getid).show();
    $("#aend_date" + getid).show();
  }
}
function selectChange(id, value) {
  getid = id.match(/\d+/)[0];
  console.log(getid)
  if (value !== "Monthly") {
    $("#dstart_date" + getid).hide();
    $("#dend_date" + getid).hide();
  } else {
    $("#dstart_date" + getid).show();
    $("#dend_date" + getid).show();
  }
}
