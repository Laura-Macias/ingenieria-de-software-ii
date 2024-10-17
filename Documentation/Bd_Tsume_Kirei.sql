USE db_tsume_kirei;
/*Se crea la base de datos relacional llamada  db_tsume_kirei para el siguiente negocio  una pagina online donde se puede agendar citas en
 un spa de uñas, para ello se crean las siguientes tablas:
 1.Tabla Calendar: Se crea esta tabla con el fin de mostrar las fechas disponibles para generar las citas.
 ATRIBUTOS 
 id_calendar: Este atributo es el identificador de la tabla (PRIMARY KEY) el cuales es de tipo ENTERO y no recibe ningun campo nulo
 event_date: Este atributo se encaraga de Guardar la fecha en la cual se agendo la cita , este atributo es de tipo DATE y no recibe campos nulo
 event_description:Este atributo acepta un adescripción del servicio que va a tomar el cliente.  
 id_customer: este es la FOREIGN KEY  entre la tabla Costumer y la Tabla Calendar.
 */
create table
  public."Calendar" (
    id_calendar integer not null,
    event_date date not null,
    event_description character varying(255) null,
    id_customer integer not null,
    constraint Calendar_pkey primary key (id_calendar),
    constraint Calendar_id_customer_fkey foreign key (id_customer) references "Customer" (id_customer)
  ) tablespace pg_default;
/*
2.Tabla Catalog:La tabla almacena información sobre los servicios o productos que ofrece el spa, como tratamientos de 
uñas u otros servicios disponibles.
Atributos:
id_catalog: Identificador único de cada producto o servicio en el catálogo.
product_name: Nombre del servicio o producto.
description: Descripción detallada del servicio o producto.
price: Precio del servicio o producto.
stock: Indica la disponibilidad de productos (si es relevante para el negocio).
update_date: Fecha y hora de la última actualización del servicio o producto en el catálogo.*/
create table
  public."Catalog" (
    id_catalog integer not null,
    product_name character varying(100) not null,
    description text null,
    price numeric(10, 3) not null,
    stock integer null default 0,
    update_date timestamp without time zone null default current_timestamp,
    constraint Catalog_pkey primary key (id_catalog)
  ) tablespace pg_default;
/*
3.Customer:La tabla almacena información detallada sobre los clientes que utilizan la plataforma para agendar citas en el spa.
Atributos:
id_customer: Identificador único del cliente.
name: Almacena el nombre del cliente.
last_name: Almacena el apellido del cliente.
email: Almacena el correo electrónico del cliente (único).
phone: Almacena el número de teléfono del cliente (único).
address: Almacena la dirección del cliente.
date: Almacena la fecha de registro del cliente.
password:Almacena la contraseña para acceder a la plataforma.
*/
create table
  public."Customer" (
    id_customer integer generated by default as identity not null,
    name character varying(100) not null,
    last_name character varying(100) not null,
    email character varying(100) not null,
    phone character varying(15) not null,
    address character varying(255) null,
    date date not null,
    password character varying not null,
    constraint Customer_pkey primary key (id_customer),
    constraint Customer_phone_key unique (phone),
    constraint cliente_email_key unique (email)
  ) tablespace pg_default;
/*
4.Tabla Staff:Esta tabla se encarga de almacenar información sobre el personal del spa, como manicuristas.
Atributos:
Id_staff: este es el identificador único del empleado el cual es de tipo Entero.
name: Nombre del empleadoel cual recibe cadenas de tipo String.
last_name: Apellido del empleado cual recibe cadenas de tipo String.
post: Cargo que desempeña dentro del spa cual recibe cadenas de tipo String.
hire_date: Fecha en que fue contratado el cual es de tipo DATE .
salary: Salario del empleado tipo Entero pero tambien resibe decimales.
id_calendar: Llave foránea que relaciona el personal con las citas programadas en el calendario.*/
create table
  public."Staff" (
    name character varying(100) not null,
    last name character varying(100) null,
    post character varying(100) null,
    hire_date date null,
    salary numeric(10, 2) null,
    "Id_ staff" integer generated by default as identity not null,
    id_calendar integer null,
    constraint Staff_pkey primary key ("Id_ staff"),
    constraint personal_Id_personal_key unique ("Id_ staff"),
    constraint Staff_id_calendar_fkey foreign key (id_calendar) references "Calendar" (id_calendar)
  ) tablespace pg_default;
/*
Tabla Transaction:su Proposito es almacenar información de las transacciones realizadas por los clientes, como pagos de citas o compra de productos.
Atributos:
account_number: Número de cuenta de la transacción (Llave primaria) el cuale es de tipo Entero.
amount: Cantidad de servicios o productos adquiridos el cuale es de tipo Entero.
total: Monto total pagado en la transacción el cuale es de tipo Entero.
transaction_date: Fecha y hora en que se realizó la transacción.
payment_method: Método de pago utilizado (efectivo, tarjeta, etc.) el cual recibe cadenas de tipo String.
bank_name: Nombre del banco asociado con el método de pago el cual recibe cadenas de tipo String.
type: Tipo de transacción (por ejemplo, 1 para pagos, 0 para reembolsos) el cuale es de tipo Entero.
id_customer: Llave foránea que relaciona la transacción con el cliente.
id_catalog: Llave foránea que relaciona la transacción con el servicio o producto del catálogo.*/
create table
  public."Transaction" (
    account_number integer not null,
    amount integer not null,
    total numeric(10, 3) not null,
    transaction_date timestamp without time zone null default current_timestamp,
    payment_method character varying(50) null,
    bank_name character varying(100) not null,
    type smallint not null,
    id_customer integer not null,
    id_catalog integer not null,
    constraint Transaction_pkey primary key (account_number),
    constraint Transaction_id_catalog_fkey foreign key (id_catalog) references "Catalog" (id_catalog),
    constraint Transaction_id_customer_fkey foreign key (id_customer) references "Customer" (id_customer)
  ) tablespace pg_default;