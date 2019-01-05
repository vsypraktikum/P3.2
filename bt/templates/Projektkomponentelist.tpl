<!-- Template -->
<!-- Projekt -->

      <table id="idList" class = "clTable">
         <tr class="listheader" class = "clTable"><th>Projekt</th><th>Beschreibung</th><th>Name</th></tr>
      @var rows_o = context['data'];@
      @for var key_s in rows_o@
         <tr id='#key_s#'>
         @var row_o = rows_o[key_s];@
            <td>#row_o['projekt']#</td><td>#row_o['beschreibung']#</td><td>#row_o['name']#</td>
         </tr>
      @endfor@
      </table>
<!-- EOF -->