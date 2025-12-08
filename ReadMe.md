Entorno Virtual y activarlo
Instalar algunas dependecias que sospecho usar
Crear el requirements.txt
Crear el gitignore
Crear la interfaz en FastApi con dos endpoints: 
    - transactions: Aqui como argumento recibe un documento en el formato especificado en models.py mediante la clase Transaction. Lo único que hace es insertar este documento.
    - /transactions/{user_id}: Aquí le damos un id de usuario y busca entre el documento para encontrar todas las transacciones del usuario y lo devuelve en una lista.
            -- database.py es para entablar la conexión con mongodb Atlas (la colección y por ende la base de datos) --
            -- models.py es para definir un tipo esquema, que en realidad es una clase pero lo uso para el primer endpoint para validar que el documento cumpla con un formato claro --
Vamos a agregar un validador con ese nombre (dejaré la referencia). En este caso lo tuve que hacer mediante Mongodb Compass, porque la interfaz web Atlas no lo tenía.
Creo un bucket en Cloud Storage, lo llamo "raw-transactions-casa-cambios", es el lugar donde Cloud Function va a guardar los JSON que reciba de MongoDB. Cada vez que MongoDB inserte un documento y el trigger lo envíe a la función, esta función creará un archivo dentro del bucket con el contenido de la transacción.
Ahora toca crear la Cloud Function "sent_to_lake" (dejaré la referencia). Lo que hace es solamente tomar la solicitud (estás intentando insertar un nuevo documento) y lo agrega al bucket (DataLake)
Ahora si el trigger "sendTransactionToGCS", que pues le manda el documento a la cloud function.

Ahora con Airflow: 
    - Extraemos archivos RAW de GCS (raw/transactions/YYYY/MM/DD/*.json).

    - Transformamos con PySpark: limpieza, normalización, agregados.

    - Validamos con Pandera: tipos y reglas de negocio.

    - Cargamos los datos limpios a BigQuery