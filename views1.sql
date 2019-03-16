-- To create VIEW for articles
CREATE VIEW articleswhicharepopular as SELECT articles.title, count(*) as views
FROM articles,log
WHERE path<>'/' AND status ='200 OK' AND articles.slug= replace(path,'/article/','')
GROUP BY articles.title
ORDER BY views desc ;

create view fault as select date(time),round(100.0*sum(case log.status
when '200 OK'  then 0 else 1 end)/count(log.status),3) as fallacy
from log 
group by date(time) 
order by fallacy desc;

create view authorswhoarepopular as select writer.name, count(log.id) as count
FROM articles artefact JOIN log ON log.path = concat('/article/', artefact.slug)
JOIN authors writer
ON writer.id = artefact.author
GROUP BY writer.name
ORDER BY count DESC ;