-- 구분 테이블 생성
CREATE TABLE GROUPS (
    -- 구분 고유번호
    GROUP_SRL NUMBER(10,0),
    -- 구분 이름
    GROUP_NAME NVARCHAR2(50) UNIQUE NOT NULL,

    -- 제약조건: 기본 키 설정
    CONSTRAINT GROUPS_GROUP_SRL_PK
    PRIMARY KEY(GROUP_SRL)
);