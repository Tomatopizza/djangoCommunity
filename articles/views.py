from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from articles.models import Article, Comment
from articles.serializers import ArticleSerializer, ArticleListSerializer, ArticleCreateSerializer, CommentSerializer, CommentCreateSerializer

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()    # 모든 글을 가져온다
        serializer = ArticleListSerializer(articles, many=True) # 모든 글을 가져오기 때문에 many=True작성
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if not request.user.is_authenticated:
            return Response("로그인 해주세요", status=status.HTTP_401_UNAUTHORIZED)
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # TODO: 위에서 if not이니까 통일성있게 할 것
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)  # id가 동일한 글을 가져온다
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article) # TODO: article 없으면 코드 진행 않고 바로 빠지기
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:    # 본인일 경우에만 글 수정
            serializer = ArticleCreateSerializer(article, data=request.data)
            if serializer.is_valid():
                serializer.save()   # TODO: 위에서 if not이니까 통일성있게 할 것
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.user:
            article.delete()    # TODO: delete가 뭔지 알아보기, delete되었을 때 리턴값을 받기 제대로 지워졌는지 확인
            return Response("삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)




class CommentView(APIView):
    def get(self, request, article_id):
        article = Article.objects.get(id=article_id)
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, article_id):
        if not request.user.is_authenticated:
            return Response("로그인 해주세요", status=status.HTTP_401_UNAUTHORIZED)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, article_id=article_id)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def put(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user: 
            serializer = CommentCreateSerializer(comment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, article_id, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user == comment.user:
            comment.delete()
            return Response("댓글이 삭제되었습니다!", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)