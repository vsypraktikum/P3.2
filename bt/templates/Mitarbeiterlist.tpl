<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Mitarbeiterverzeichnis
   </h2>
   <div id="idContentArea" class="clContentArea">
      <table id="idList" class = "clTable">
         <tr class="listheader"><th>Name</th><th>Vorname</th><th>Alter</th><th>Abteilung</th></tr>
      @var rows_o = context['data'];@
      @for var key_s in rows_o@
         <tr id='#key_s#'>
         @var row_o = rows_o[key_s];@
            <td>#row_o['name']#</td><td>#row_o['vorname']#</td><td>#row_o['alter']#</td><td>#row_o['abteilung']#
         </tr>
      @endfor@
      </table>
   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="add" class="clButton">Hinzufügen</button>
      <button data-action="edit" class="clButton">Bearbeiten</button>
      <button data-action="delete" class="clButton">Löschen</button>
   </div>
</div>