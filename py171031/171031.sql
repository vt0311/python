-- 모든 학생의 아이디, 이름, 생일, 과목, 점수를 출력하되,
-- 아이디의 역순으로 정렬하시오
select students.id, students.name, students.birth, sungjuk.subject, sungjuk.jumsu
from students join sungjuk
on students.id = sungjuk.id
order by students.id desc ;

-- 별칭을 사용하는 경우
select st.id, st.name, st.birth, sg.subject, sg.jumsu
from students st join sungjuk sg
on st.id = sg.id
order by st.id desc ;

-- in 연산자
-- 아이디가 'lee', 'jo'인 학생
select id, name, birth
from students where id in('lee', 'jo');

-- 아이디가 'lee', 'jo'인 학생의 이름, 과목, 점수를 출력
select st.name, sg.subject, sg.jumsu
from students st join sungjuk sg
on st.id = sg.id
and st.id in('lee', 'jo');

-- html 점수가 10점인 학생의 이름은 무엇인가?
select name from students 
where id = ( 
		select id 
		from sungjuk 
		where subject = 'html'
		and jumsu = 10 );


-- 모든 학생의 성적의 총합은 각각 얼마인가?
select id, sum(jumsu)
from sungjuk
group by id ;

-- 모든 학생의 성적의 총합 중 100점이 넘는 학생들만 조회
select id, sum(jumsu)
from sungjuk
group by id 
having sum(jumsu) >= 100;