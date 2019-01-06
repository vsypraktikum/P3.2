<!-- Template -->
<form id="idForm" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Komponentenverzeichnis / Formular
   </h2>
   <div id="idContentArea" class="clContentArea">

   <input type="hidden" value="#context.data.id#" id="id_s" name="id_s" />
   <div class="clFormRow">
      <label for="name_s">Name <span class="clRequired"></span></label>
      <input type="text" value="#context.data.name#" id="name_s" name="name_s" autofocus required />
   </div>
   <div class="clFormRow">
      <label for="beschreibung_s">Beschreibung <span class="clRequired"></span></label>
      <input type="text" value="#context.data.beschreibung#" id="beschreibung_s" name="beschreibung_s" required />
   </div>
   <div class="clFormRow" id="selecter">
      <label for="projekt_s">Projekt <span class="clRequired"></span></label>
         @var rows_pro = context['data_projekt'];@
         <select id="projekt_s" name="projekt_s">
            @for var key_pro in rows_pro@
                  @var row_pro = rows_pro[key_pro];@
                  <option value="#row_pro['name']#">#row_pro['name']# </option>
            @endfor@
         </select>
   </div>
   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="back" class="clButton">Zurück</button>
      <button data-action="save" class="clButton">Speichern</button>
   </div>
</form>
<!-- EOF -->
