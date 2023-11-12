CREATE TABLE IF NOT EXISTS public.subscriptions
(
    username character varying(255) COLLATE pg_catalog."default" NOT NULL,
    payment_method character varying(255) COLLATE pg_catalog."default",
    plan character varying(255) COLLATE pg_catalog."default",
    status character varying(255) COLLATE pg_catalog."default",
    term character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT subscriptions_pkey PRIMARY KEY (username)
)

ALTER TABLE IF EXISTS public.subscriptions
    OWNER to postgres;