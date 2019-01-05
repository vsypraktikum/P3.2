<!-- Template -->
<!-- Projekt -->

      <table id="idList" class = "clTable">
         <tr class="listheader"><th>Komponente</th></th><th>Beschreibung</th><th>Mitarbeiter</th><th>Datum</th><th>Kategorie</th><th>Fehlerstatus</th></tr>
      @var rows_o = context['data'];@
      @for var key_s in rows_o@
         <tr id='#key_s#'>
         @var row_o = rows_o[key_s];@
            <td>#row_o['komponente']#</td><td>#row_o['beschreibung']#</td><td>#row_o['mitarbeiter']#</td><td>#row_o['datum']#</td><td>#row_o['kategorie']#</td><td>#row_o['fehlerstatus']#</td>
         </tr>
      @endfor@
      </table>
<!-- EOF -->