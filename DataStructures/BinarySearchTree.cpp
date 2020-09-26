#include<iostream>

using namespace std;



struct BstNode
{
    int val;
    BstNode* left;
    BstNode* right;
};

BstNode* getNewNode(int val)
{
    BstNode* node = new BstNode();
    node->val = val;
    node->left = NULL;
    node->right = NULL;
}


BstNode* insert(BstNode* root, int data)
{
    if(root == NULL)
    {
        root = getNewNode(data);
        
    } else if(data <= root->val)
    {
        root->left = insert(root->left, data);
    } else {
        root->right = insert(root->right, data);
    }
    return root;
}



int main()
{
    BstNode* root = new BstNode();
    root = NULL;

    root = insert(root, 10);
    root = insert(root, 15);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 5);
    root = insert(root, 80);
    return 0;
}
