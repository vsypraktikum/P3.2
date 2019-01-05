<!-- Template -->
@let loop_i;@
@for loop_i=0; loop_i < context.length; loop_i++@
<a href="##" data-action="#context[loop_i].action#">#context[loop_i].text#</a>
@endfor@

