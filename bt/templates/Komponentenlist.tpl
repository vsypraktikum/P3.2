<!-- Template -->
<!-- Projekt -->
<div id="idListContent" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Komponentenverzeichnis
   </h2>
   <div id="idContentArea" class="clContentArea">
      <table id="idList" class = "clTable">
         <tr class="listheader" class = "clTable"><th>Name</th><th>Beschreibung</th><th>Projekt</th></tr>
      @var rows_o = context['data'];@
      @for var key_s in rows_o@
         <tr id='#key_s#'>
         @var row_o = rows_o[key_s];@
            <td>#row_o['name']#</td><td>#row_o['beschreibung']#</td><td>#row_o['projekt']#</td>
         </tr>
      @endfor@
      </table>
   </div>
   <div id = "idContentArea2" class="clContentArea_2"></div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="add" class="clButton">Hinzufügen</button>
      <button data-action="edit" class="clButton">Bearbeiten</button>
      <button data-action="delete" class="clButton">Löschen</button>
      <select id = "projekt_name" name>
         @var rows_proj = context['data_projekt'];@
         @for var key_p in rows_proj@
            @var row_proj = rows_proj[key_p];@
            <option value="#key_p#">#row_proj['name']# </option>
         @endfor@
      </select>
      <button data-action="sort" class="clButton">Sortieren</button>
   </div>
</div>

<!-- EOF -->