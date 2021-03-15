-- MySql --

-- 데이터 베이스 생성. --
create database pusan_board_db
default character set utf8
collate utf8_unicode_ci;


-- 데이터 베이스 사용 설정. --
use pusan_board_db;


-- 회원정보 테이블(user table) --

create table user_table(
    -- 사용자 번호 --
    -- auto_increment : 자동 1씩 증가. --
    user_idx int auto_increment,
    -- 사용자 이름 --
    user_name char(10) not null,
    -- 사용자 아이디 --
    user_id varchar(100) not null,
    -- 사용자 비밀번호 --
    user_pw varchar(100) not null,
    -- primary key (기본키) : 각 행을 고유하게 식별하는 역할. -
    constraint user_pk primary key(user_idx),
    -- unique() : 제약 조건의 하나로 해당 컬럼에 동일한 값이 들어가지 않도록함. --
    constraint user_unique unique(user_id)
);


-- 게시판 테이블(board_table) -- 

create table board_table(
    -- 게시판 인덱스 --
    board_idx int auto_increment,
    -- 게시판 이름 --
    board_name varchar(100) not null,
    constraint board_pk primary key(board_idx),
    constraint board_unique unique(board_name)
);


-- 게시글 테이블(content_table) -- 

create table content_table(
    -- 글 번호 --
    content_idx int auto_increment,
    -- 글 제목 --
    content_subject varchar(500) not null,
    -- 작성 날짜 --
    content_date date not null,
    -- 작성자 인덱스 --
    content_writer_idx int not null,
    -- 글 내용 --
    content_text varchar(500) not null,
    -- 첨부 이미지 --
    -- 첨부 이미지가 굳이 필요 없으므로 null 허용 시킬 것.
    content_file varchar(500),
    -- 게시판 인덱스 --
    content_board_idx int not null,
    -- 글 번호 기본키(pk) 설정 --
    constraint content_pk primary key(content_idx),
    -- foreign key (외래키) : 한 테이블의 필드 중 다른 테이블의 행을 식별할 수 있는 키. --
    -- 작성자 인덱스 외래키(fk) 설정 --
    constraint content_fk1 foreign key(content_writer_idx)
    references user_table(user_idx),
    -- 게시판 인덱스 외래키(fk) 설정 --
    constraint content_fk2 foreign key(content_board_idx)
    references board_table(board_idx)
);


# 게시판 테이블 데이터.

insert into board_table (board_name) values ('자유게시판');
insert into board_table (board_name) values ('유머게시판');
insert into board_table (board_name) values ('정치게시판');
insert into board_table (board_name) values ('스포츠게시판');

commit;
