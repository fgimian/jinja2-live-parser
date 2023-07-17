$(document).ready(function(){
    function render_template() {
        var useAnsibleFilters = $('input[id="use-ansible-filters"]').is(':checked') ? 1:0;
        var trimBlocks = $('input[id="trim-blocks"]').is(':checked') ? 1:0;
        var lstripBlocks = $('input[id="lstrip-blocks"]').is(':checked') ? 1:0;
        var showWhitespace = $('input[id="show-whitespace"]').is(':checked') ? 1:0;
        $.post('/render', {
            template: $('#template').val(),
            values: $('#values').val(),
            use_ansible_filters: useAnsibleFilters,
            trim_blocks: trimBlocks,
            lstrip_blocks: lstripBlocks
        }).done(function(response) {
            if (showWhitespace) {
                response = response.replace(/ /g, String.fromCharCode(parseInt(387, 16)));
            }
            $('#render').val(response);
        });
    }

    $('#template').on('change keyup paste', function() {
        render_template();
    });

    $('#values').on('change keyup paste', function() {
        render_template();
    });

    $('#use-ansible-filters,#trim-blocks,#lstrip-blocks,#show-whitespace').on('change', function() {
        render_template();
    });
});
