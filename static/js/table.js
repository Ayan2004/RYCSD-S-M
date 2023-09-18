let minDate, maxDate;

let col = 4
console.log(col);

// Custom filtering function which will search data in column four between two values
DataTable.ext.search.push(function (settings, data, dataIndex) {
    let min = minDate.val();
    let max = maxDate.val();
    let date = new Date(data[col]);
 
    if (
        (min === null && max === null) ||
        (min === null && date <= max) ||
        (min <= date && max === null) ||
        (min <= date && date <= max)
    ) {
        return true;
    }
    return false;
});
 
// Create date inputs
minDate = new DateTime('#min', {
    format: 'MMMM Do YYYY'
});
maxDate = new DateTime('#max', {
    format: 'MMMM Do YYYY'
});
 
// DataTables initialisation
// let table = new DataTable('#myTable');




let table = new DataTable('#myTable', {
    responsive: true,
    retrieve: true,
    columnDefs: [
        { "width": "20%", "targets": 3 }
    ],
    
    dom: 'lBfrtip', 
    // dom: 'Bfrtip',
    buttons: true,
    buttons: [
        {
        extend:    'csv',
        text:      '<i class="fa fa-files-o"></i> CSV',
        titleAttr: 'CSV',
        className: 'btn btn-default btn-sm',
        exportOptions: {
            columns: ':visible'
        }
        },
        {
        extend:    'excel',
        text:      '<i class="fa fa-files-o"></i> Excel',
        titleAttr: 'Excel',
        className: 'btn btn-default btn-sm',
        exportOptions: {
            columns: ':visible'
        }
        },
        {
        extend:    'pdf',
        text:      '<i class="fa fa-file-pdf-o"></i> PDF',
        titleAttr: 'PDF',
        className: 'btn btn-default btn-sm',
        exportOptions: {
            columns: ':visible'
        }
        },               
        {
        extend:    'print',
        text:      '<i class="fa fa-print"></i> Print',
        titleAttr: 'Print',
        className: 'btn btn-default btn-sm',
        exportOptions: {
            columns: ':visible'
        }
        },  
    ]
    
} );


let table2 = new DataTable('#feepayTable', {
    order: [],
    responsive: true,
    retrieve: true,
    paging: false,
});




 
// Refilter the table
document.querySelectorAll('#min, #max').forEach((el) => {
    el.addEventListener('change', () => table.draw());

});



  

  