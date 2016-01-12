/**
 * Controller class for AnalysisRequest add view
 */
function CustomAnalysisRequestAddView() {

    var that = this;

    this.load = function() {

        // https://jira.bikalabs.com/browse/WINE-66
        // I will insert 'SampleType_hidden' key into all state variables.
        // This allows me to include a default SampleType value in all ar columns,
        // without requiring the rest of the column to be filled out.
        var keys = Object.keys(window.bika.lims.ar_add.state);
        for(var arnum=0; arnum < keys.length; arnum++){
            window.bika.lims.ar_add.state[arnum]['SampleType_hidden'] = 1;
        }
    };

}
