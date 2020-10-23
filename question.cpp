class Country{
  private: int  population;
  public:
    void setPop(int pop){
      this->population = pop;
    }
    int getPop(){
      return this->population;
    }
};
class India: private Country{};
int main(){
  India obj;
  obj.setPop(750);
  cout<<obj.getPop()<<endl;
  return 0;
}
