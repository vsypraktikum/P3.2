<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Bearbeitung Fehlerdaten
   </h2>
   <div id="idContentArea" class="clContentArea">
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
   </div>
   <div id = "idContentArea2" class="clContentArea_2"></div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="add" class="clButton">Hinzufügen</button>
      <button data-action="edit" class="clButton">Bearbeiten</button>
      <button data-action="delete" class="clButton">Löschen</button>
      <button data-action="auswerten_erkannt" id = "fehler_erkannt" value="erkannt" class="clButton">Bekannte auswerten</button>
      <button data-action="auswerten_behoben" id = "fehler_behoben" value="behoben" class="clButton">Behobene auswerten</button>
   </div>
</div>