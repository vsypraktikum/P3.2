<form id="idForm" class="clContent">
   <h2 id="idContentHeader" class="clContentHeader">
      Bearbeitung Mitarbeiter / Formular
   </h2>
   <div id="idContentArea" class="clContentArea">

   <input type="hidden" value="#context.data.id#" id="id_s" name="id_s" />
    <div class="clFormRow">
      <label for="name_s">Name <span class="clRequired"></span></label>
      <input type="text" value="#context.data.name#" id="name_s" name="name_s" autofocus required />
   </div>
   <div class="clFormRow">
      <label for="vorname_s">Vorname <span class="clRequired"></span></label>
      <input type="text" value="#context.data.vorname#" id="vorname_s" name="vorname_s" required />
   </div>
   <div class="clFormRow">
      <label for="alter_s">Alter <span class="clRequired"></span></label>
      <input type="text" value="#context.data.alter#" id="alter_s" name="alter_s" required />
   </div>
   <div class="clFormRow" id="selecter">
      <p>Abteilung:</p>
      <select id="abteilung_s" name="abteilung_s">
         <option value = "SW">SW</option>
         <option value = "QS">QS</option>
      </select>
   </div>
   </div>
   <div id="idButtonArea" class="clButtonArea">
      <button data-action="back" class="clButton">Zurück</button>
      <button data-action="save" class="clButton">Speichern</button>
   </div>
</form>